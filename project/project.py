import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from digital_twin_distiller import ml_project
from digital_twin_distiller.modelpaths import ModelDir
from preprocessing import PreprocessInput
from predict import PredictSentiment
from digital_twin_distiller.encapsulator import Encapsulator

class SentimentAnalyzerProject(ml_project.MachineLearningProject):

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
    ModelDir.set_base(__file__)

    # runs the project server
    app = SentimentAnalyzerProject(app_name="Sentiment Analyzer based on Distiller", no_cache=True)

    # pp = Path("../docs").absolute()

    server = Encapsulator(app)
    server.build_docs()
    server.run()
    # server.set_project_mkdocs_dir_path(pp)

    # Mounting folders of the default mkdocs documentation to the application.
    # server.app.mount(
    #     "/images",
    #     StaticFiles(directory=files("docs") / "site" / "images"),
    #     name="images",
    # )


    # server.host = "127.0.0.1"
    # server.run()
