import pickle
from importlib_resources import files


class PredictSentiment:
    def run(self, input_data: dict):
        text = input_data["text"]
        decision = self.predict_emotion(text)[0]
        return str(decision)

    @staticmethod
    def predict_emotion(text: str) -> str:
        """
        Method for loading predefined Support Vector Machine model and TF-IDF vectorizer, and predict sentiment (emotion)
         class for the input sentence

        :param text: Sentence to predict
        :return: Predicted label
        """


        tfidf = files("resources") / 'Multiclass_case' / 'Sentiment_vectoriser.pickle'
        svm_pretrained = files("resources") / 'Multiclass_case' / 'Sentiment_model.sav'

        v = open(tfidf, 'rb')
        m = open(svm_pretrained, 'rb')

        vectorized = pickle.load(v)
        svc_cmodel = pickle.load(m)

        transformed = vectorized.transform([text])
        result = svc_cmodel.predict(transformed)

        v.close()
        m.close()

        return result
