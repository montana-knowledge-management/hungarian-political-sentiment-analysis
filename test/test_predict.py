import unittest

from project.predict import PredictSentiment

class PredistionTestCase(unittest.TestCase):
    def test_sentence_without_emotion(self):

        svm = PredictSentiment()
        predicted_emotion = svm.predict_emotion("Magyarországon jelenleg több mint 1 millió ember él magányosan, ebből több mint 600 ezer 65 év feletti.")
        expected_emotion = "Semleges"
        self.assertEqual(predicted_emotion, expected_emotion)

    def test_sentence_with_negative_emotion(self):

        svm = PredictSentiment()
        predicted_emotion = svm.predict_emotion("A European Social Survey 2019-es kutatása szerint a hazai helyzet siralmas: "
                                                "a felmérésben megkérdezettek több mint 10 százaléka érezte magányosnak magát, "
                                                "és a felnőtt lakosság 40 százaléka nem, vagy csak alig él társadalmi életet: családjával, "
                                                "barátaival egy hónapban csupán egyszer, vagy egyszer sem találkozik.")
        expected_emotion = "Negativ"
        self.assertEqual(predicted_emotion, expected_emotion)


    def test_sentence_positive_emotion(self):

        svm = PredictSentiment()
        predicted_emotion = svm.predict_emotion("A Francia Természettudományi Akadémia (Académie des sciences) külső tagjává választották "
                                                "Karikó Katalint, akinek odaítélték a svéd Camurus Lipidkutatási Alapítvány kitüntetését is.")
        expected_emotion = "Pozitiv"
        self.assertEqual(predicted_emotion, expected_emotion)