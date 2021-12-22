import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from distiller.concept import AbstractProject
from preprocessing import PreprocessInput
from predict import PredictSentiment
from pathlib import Path
from distiller.server import Server
from importlib_resources import files
from fastapi.staticfiles import StaticFiles


class SentimentAnalyzerProject(AbstractProject):

    def custom_input(self, input_dict : dict):
        self._input_data.append(input_dict)

    def run(self):
        document = self._input_data[0]
        original_text = document['text']
        preprocessor = PreprocessInput()
        preprocessed_document = preprocessor.run(document) #preprocess
        predictor = PredictSentiment()
        predicted_label = predictor.run(preprocessed_document)
        result = {'text' : original_text, 'label' : predicted_label}
        self._output_data = [result]


if __name__ == "__main__":
    # runs the project server
    app = SentimentAnalyzerProject(app_name="Sentiment Analyzer based on Distiller", no_cache=True)

    pp = Path("../docs").absolute()

    server = Server(app)
    server.set_project_mkdocs_dir_path(pp)

    # Mounting folders of the default mkdocs documentation to the application.
    server.app.mount(
        "/images",
        StaticFiles(directory=files("docs") / "site" / "images"),
        name="images",
    )

    server.host = "127.0.0.1"
    server.run()
