from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="distiller-sentiment-analysis-2021-1",
    install_requires=[
        "pre-commit",
        "matplotlib",
        "pandas",
        "numpy",
        "sklearn2json @ git+https://bitbucket.org/montanatudasmenedzsmentkft/sklearn2json.git#egg=Sklearn2JSON",
        "distiller @ git+https://bitbucket.org/montanatudasmenedzsmentkft/distiller.git#egg=Distiller==2021.6.2",
        "tqdm",
        "sklearn",
        "cyhunspell",
        "importlib_resources",
        "tika",
        "regex",
        "roman",
        "python-Levenshtein",
    ],
)
