import unittest
from project.project import SentimentAnalyzerProject


class ProjectTestCase(unittest.TestCase):

    def test_project(self):
        analyzer = SentimentAnalyzerProject()
