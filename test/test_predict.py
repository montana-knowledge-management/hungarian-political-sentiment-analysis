import unittest
import json
from importlib_resources import files

from project.predict import PredictSentiment

class PredistionTestCase(unittest.TestCase):
    def test_predictions(self):

        path = files("resources") / 'Test_cases' / 'disgust.json'
        dictionary = dict()
        with open(path) as json_file:
            dictionary = json.load(json_file)

        svm = PredictSentiment()
        predicted_emotion = svm.predict_emotion(dictionary['text'])
        expected_emotion = dictionary["label"]

        self.assertTrue(dictionary)
        self.assertEqual(predicted_emotion, expected_emotion)

