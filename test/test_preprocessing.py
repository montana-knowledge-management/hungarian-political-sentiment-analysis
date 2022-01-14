import unittest

from project.preprocessing import PreprocessInput


class PreprocessingTestCase(unittest.TestCase):
    def test_stopword_removal(self):
        test_text = "ez egy\nnagy minta"
        preprocessor = PreprocessInput()
        stopword_cleaned = preprocessor.cleaning_stopwords(test_text)
        self.assertNotIn("ez", stopword_cleaned)
        self.assertNotIn("\n", stopword_cleaned)

    def test_number_removal(self):
        test_text = "ez egy\nnagy minta amiben van 123 szám is"
        preprocessor = PreprocessInput()
        number_cleaned = preprocessor.cleaning_numbers(test_text)
        self.assertIn("ez", number_cleaned)
        self.assertIn("\n", number_cleaned)
        self.assertNotIn("123", number_cleaned)
        self.assertEqual("ez egy\nnagy minta amiben van  szám is", number_cleaned)

    def test_punctuation_removal(self):
        test_text = "Példa szöveg\", sok központ.ozással!?"
        preprocessor = PreprocessInput()
        punctuation_cleaned = preprocessor.cleaning_punctuations(test_text)
        self.assertEqual("Példa szöveg sok központozással", punctuation_cleaned)

    def test_monspell_stemmer(self):

        test_text = ['korábban', 'független', 'fenyegetést', 'akceptálni']
        expected_text = ['korább', 'független', 'fenyegetés', 'akceptál']

        preprocessor = PreprocessInput()
        actual_text = list()
        for token in test_text:
            stem = preprocessor.hungarian_stemmer_stem(token)
            actual_text.append(stem.strip())

        self.assertTrue(actual_text)
        self.assertListEqual(expected_text, actual_text)

    def test_run(self):
        test_text = {"text" : "elkövetőknek"}
        preprocessor = PreprocessInput()
        result = preprocessor(test_text)

        self.assertEqual(test_text["text"].strip(), 'elkövető')


if __name__ == "__main__":
    unittest.main()
