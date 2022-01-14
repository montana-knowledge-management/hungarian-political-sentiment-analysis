import unittest
import json
from importlib_resources import files

from project.predict import PredictSentiment

class PredistionTestCase(unittest.TestCase):
    def test_sentence_with_negative_emotion(self):

        #külön teszt mondatokkal poz/neg/neutral -- mindere egy-egy def_poz_sentence -- elnevezes

        svm = PredictSentiment()

        path = files("resources") / 'Test_cases' / 'disgust.json'
        dictionary = dict()
        with open(path) as json_file:
            dictionary = json.load(json_file)


        predicted_emotion = svm.predict_emotion(dictionary['text'])
        expected_emotion = dictionary["label"]

        self.assertTrue(dictionary)
        self.assertEqual(predicted_emotion, expected_emotion)

    def test_sentence_with_positive_emotion(self):
        pass

    def test_sentence_without_emotion(self):
        pass