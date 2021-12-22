import numpy.random
import pandas as pd
from importlib_resources import files
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, f1_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

RANDOM_STATE = 1
np.random.seed(RANDOM_STATE)


def split_train_test(Xa, Xd):
    Xa_train, Xa_test, ya_train, ya_test = train_test_split(Xa.Full_text_processed,
                                                            Xa.Label, test_size=0.20,
                                                            random_state=26105111)
    Xd_train, Xd_test, yd_train, yd_test = train_test_split(Xd.Full_text_processed,
                                                            Xd.Label, test_size=0.20,
                                                            random_state=26105111)

    y_test = ya_test.append(yd_test).values
    X_test = Xa_test.append(Xd_test)
    return Xa_train, ya_train, Xd_train, yd_train, X_test, y_test


def get_subsample(Xa_train, Xd_train, ya_train, yd_train, subset_size):
    indices = np.random.choice(len(Xd_train), subset_size, replace=False)
    Xd_train_aug = Xd_train.iloc[indices]
    X_train = Xa_train.append(Xd_train_aug)
    yd_train_aug = yd_train.iloc[indices]
    y_train = ya_train.append(yd_train_aug)
    return X_train, y_train


def repeated_augmentation(Xa_train, Xd_train, ya_train, yd_train, subset_size, augment_to):
    indices = np.random.choice(len(Xd_train), subset_size, replace=False)
    factor = int(np.ceil(augment_to / subset_size))
    Xd_train_aug = Xd_train.iloc[indices].repeat(factor)
    X_train = Xa_train.append(Xd_train_aug[:augment_to])
    yd_train_aug = yd_train.iloc[indices].repeat(factor)
    y_train = ya_train.append(yd_train_aug[:augment_to])
    return X_train, y_train


def iterate_through_datasets_augmented(Xa_train, ya_train, Xd_train, yd_train, X_test, y_test, dataset_name):
    base_pat = re.compile(r"for(\d+)")
    alpha_pat = re.compile(r"_(\d\.\d)_")
    aug_type_pat = re.compile(r"[A-Z]{2}|[13]00D")
    for subset_size in [len(Xd_train)]:  #
        results_f1_d = []
        results_p_d = []
        results_r_d = []
        results_f1_a = []
        results_p_a = []
        results_r_a = []
        avg_vocab_lengths = []
        for i in range(1):
            X_train, y_train = get_subsample(Xa_train, Xd_train, ya_train, yd_train, subset_size)
            # print(len(X_train))
            assert X_train.shape[0] == 720 + subset_size  # 1441,02
            assert X_test.shape[0] == 360
            assert y_test.shape[0] == 360
            assert y_train.shape[0] == 720 + subset_size  # 1440
            vectorizer = TfidfVectorizer(ngram_range=(1, 2))

            vectorizer.fit(X_train)

            X_train_vec = vectorizer.transform(X_train)
            X_test_vec = vectorizer.transform(X_test)

            svc = LinearSVC(class_weight="balanced", random_state=RANDOM_STATE, max_iter=10000, tol=1e-5)
            model = svc.fit(X_train_vec, y_train)
            y_pred = model.predict(X_test_vec)
            f1_d = f1_score(y_test, y_pred, pos_label="Disgust")
            r_d = recall_score(y_test, y_pred, pos_label="Disgust")
            p_d = precision_score(y_test, y_pred, pos_label="Disgust")
            f1_a = f1_score(y_test, y_pred, pos_label="Anticipation")
            r_a = recall_score(y_test, y_pred, pos_label="Anticipation")
            p_a = precision_score(y_test, y_pred, pos_label="Anticipation")

            results_f1_d.append(f1_d)
            results_p_d.append(p_d)
            results_r_d.append(r_d)
            results_f1_a.append(f1_a)
            results_p_a.append(p_a)
            results_r_a.append(r_a)
            avg_vocab_lengths.append(len(vectorizer.vocabulary_))

        results_f1_d = np.array(results_f1_d)
        results_p_d = np.array(results_p_d)
        results_r_d = np.array(results_r_d)

        results_f1_a = np.array(results_f1_a)
        results_p_a = np.array(results_p_a)
        results_r_a = np.array(results_r_a)
        avg_vocab_lengths = np.array(avg_vocab_lengths)
        res = [results_p_a, results_r_a, results_f1_a, results_p_d, results_r_d, results_f1_d]
        # result = ["{:.2f}\t{:.2f}".format(np.mean(calc) * 100, np.std(calc) * 100) for calc in res]
        result = ["{:.2f}".format(np.mean(calc) * 100).replace(".", ",") for calc in res]

        base = base_pat.search(dataset_name).group(1)
        alpha = alpha_pat.search(dataset_name).group(1)
        aug_type = aug_type_pat.search(dataset_name).group(0)
        result = [dataset_name.replace("for", "").replace("_.txt", "").replace(".txt", "")] + result + [aug_type, alpha,
                                                                                                        base,
                                                                                                        "{:.2f}".format(
                                                                                                            np.mean(
                                                                                                                avg_vocab_lengths)).replace(
                                                                                                            ".", ",")]
        print("\t".join(result))
        # print("------------------------------\nSubset size: {}\n------------------------------".format(subset_size))
        # print("{:.2f}\t{:.2f}".format(np.mean(results) * 100, np.std(results) * 100))
        # print("{:.2f}\t{:.2f}".format(np.mean(avg_vocab_lengths), np.std(avg_vocab_lengths)))


def iterate_through_datasets_base(Xa_train, ya_train, Xd_train, yd_train, X_test, y_test, dataset_name):
    for subset_size in [10, 25, 50, 100, 250, 500, len(Xd_train)]:  #
        results_f1_d = []
        results_p_d = []
        results_r_d = []
        results_f1_a = []
        results_p_a = []
        results_r_a = []
        avg_vocab_lengths = []
        for i in range(100):
            X_train, y_train = get_subsample(Xa_train, Xd_train, ya_train, yd_train, subset_size)
            # print(len(X_train))
            assert X_train.shape[0] == 719 + subset_size  # 1441,02
            assert X_test.shape[0] == 360
            assert y_test.shape[0] == 360
            assert y_train.shape[0] == 719 + subset_size  # 1440
            vectorizer = TfidfVectorizer(ngram_range=(1, 2))

            vectorizer.fit(X_train)

            X_train_vec = vectorizer.transform(X_train)
            X_test_vec = vectorizer.transform(X_test)

            svc = LinearSVC(class_weight="balanced", random_state=RANDOM_STATE, max_iter=10000, tol=1e-5)
            model = svc.fit(X_train_vec, y_train)
            y_pred = model.predict(X_test_vec)
            f1_d = f1_score(y_test, y_pred, pos_label="Disgust")
            r_d = recall_score(y_test, y_pred, pos_label="Disgust")
            p_d = precision_score(y_test, y_pred, pos_label="Disgust")
            f1_a = f1_score(y_test, y_pred, pos_label="Anticipation")
            r_a = recall_score(y_test, y_pred, pos_label="Anticipation")
            p_a = precision_score(y_test, y_pred, pos_label="Anticipation")

            results_f1_d.append(f1_d)
            results_p_d.append(p_d)
            results_r_d.append(r_d)
            results_f1_a.append(f1_a)
            results_p_a.append(p_a)
            results_r_a.append(r_a)
            avg_vocab_lengths.append(len(vectorizer.vocabulary_))

        results_f1_d = np.array(results_f1_d)
        results_p_d = np.array(results_p_d)
        results_r_d = np.array(results_r_d)

        results_f1_a = np.array(results_f1_a)
        results_p_a = np.array(results_p_a)
        results_r_a = np.array(results_r_a)
        avg_vocab_lengths = np.array(avg_vocab_lengths)
        res = [results_p_a, results_r_a, results_f1_a, results_p_d, results_r_d, results_f1_d]
        result = ["{:.2f}\t{:.2f}".format(np.mean(calc) * 100, np.std(calc) * 100).replace(".", ",") for calc in res]

        result = [str(subset_size),
                  dataset_name.replace("for", "").replace("_.txt", "").replace(".txt", "")] + result + [
                     "{:.2f}\t{:.2f}".format(np.mean(avg_vocab_lengths), np.std(avg_vocab_lengths)).replace(".", ",")]
        print("\t".join(result))
        # print("------------------------------\nSubset size: {}\n------------------------------".format(subset_size))
        # print("{:.2f}\t{:.2f}".format(np.mean(results) * 100, np.std(results) * 100))
        # print("{:.2f}\t{:.2f}".format(np.mean(avg_vocab_lengths), np.std(avg_vocab_lengths)))


if __name__ == "__main__":
    AUG_SIZE = 720

    # data = pd.read_excel(files("resources") / 'Control_DATA_combined.xlsx')
    # data = pd.read_excel(files("resources") / 'ALL_DATA_hunstemmed.xlsx')
    # data = pd.read_excel(files("resources") / 'ALL_DATA_lemmatized.xlsx')
    data = pd.read_excel(files("resources") / 'ALL_DATA_monstemmed.xlsx')

    print(data.shape)
    print(data.info())
    print(data.head())

    """# For augmented data:"""

    original = data.iloc[:7199]
    augmented = data.iloc[7200:]
    # print(original.shape, augmented.shape)
    print(augmented.Source.unique())
    # 8
    anticipation_original = original[original.Source == 'anticipation_original']
    disgust_original = original[original.Source == 'disgust_original']

    anticipation_original_hunstemmed = original[original.Source == 'anticipation_original_hunspell_stemmed']
    disgust_original_hunstemmed = original[original.Source == 'disgust_original_hunspell-stemmed']

    anticipation_original_monstemmed = original[original.Source == 'anticipation_original_monstemmed']
    disgust_original_monstemmed = original[original.Source == 'disgust_original_monstemmed']

    anticipation_original_Lemmatized = original[original.Source == 'anticipation_original_lemmatized']
    disgust_original_Lemmatized = original[original.Source == 'disgust_original_lemmatized']

    Xa = anticipation_original_monstemmed
    Xd = disgust_original_monstemmed
    print(Xd.Source.unique())
    Xa_train, ya_train, Xd_train, yd_train, X_test, y_test = split_train_test(Xa, Xd)
    iterate_through_datasets_base(Xa_train, ya_train, Xd_train, yd_train, X_test, y_test, dataset_name=Xd.Source.unique()[0])
    length = augmented.shape[0] // 900
    # for i in range(length):
    #     Xd = augmented.iloc[i * 900:(i * 900 + 899)]
    #     # print(Xd.Source.unique())
    #     # print(Xd.info())
    #     # print(Xd.head(200))
    #     Xd_train = Xd.Full_text_processed[:AUG_SIZE]
    #     yd_train = Xd.Label[:AUG_SIZE]
    #     # print(Xa_train.iloc[50], ya_train.iloc[50])
    #     iterate_through_datasets_augmented(Xa_train, ya_train, Xd_train, yd_train, X_test, y_test,
    #                                        dataset_name=Xd.Source.unique()[0])
