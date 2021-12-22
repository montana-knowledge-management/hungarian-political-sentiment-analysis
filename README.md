# Sentiment Analyzer README #

# Dockerization

The dockerization needs the following changes/modifications in the project:

* dockerize.sh: the first two lines should be rewritten, according to the name of the project.
* Dockerfile: the only task is to give the name of the project folders (e.g. \project, \extractors,...) and the command,
  which runs the project, the file automatically copies the files and directories to the defined structure and runs the
  project automatically.
* the following lines should be added to the beginning of the project file, because the docker runs the project directly
  from the project folder:

```
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
```
