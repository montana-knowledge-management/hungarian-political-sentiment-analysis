import pickle
from importlib_resources import files

class PredictSentiment():
    def run(self, input_data : dict):
        text = input_data["text"]
        decision = self.predict_emotion(text)[0]
        return str(decision)

    @staticmethod
    def predict_emotion(text :str):

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