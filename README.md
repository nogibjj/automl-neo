[![build](https://github.com/shyamal-anadkat/automl-neo/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/shyamal-anadkat/automl-neo/actions/workflows/main.yml)

# AutoML NEO (Nearest Earth Objects)

Auto ML solution using two open-source frameworks:

1. [Ludwig](https://ludwig-ai.github.io/ludwig-docs/0.5/index.html),
a declarative deep learning framework that allows users to train, evaluate, and deploy models without the need to write code.
2. [FLAML](https://github.com/microsoft/FLAML), 
a lightweight Python library from Microsoft that finds accurate machine learning models automatically, efficiently and economically. It frees users from selecting learners and hyperparameters for each learner.

## Dataset

[NASA - Nearest Earth Objects](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects?datasetId=2272878&sortBy=voteCount&select=neo.csv)

>There is an infinite number of objects in the outer space. Some of them are closer than we think. Even though we might think that a distance of 70,000 Km can not potentially harm us, but at an astronomical scale, this is a very small distance and can disrupt many natural phenomena. These objects/asteroids can thus prove to be harmful. Hence, it is wise to know what is surrounding us and what can harm us amongst those. Thus, this dataset compiles the list of NASA certified asteroids that are classified as the nearest earth object.

## Development 

Creating virtual environment:

 1. ```python3 -m venv venv```
 2.  (On Unix or MacOS) ```source venv/bin/activate```

Then run:
```bash
 chmod +x run_automl_flaml.py
 chmod +x run_automl_ludwig.py
```

### Contributing guidelines:

Run ```make all``` before pushing code.

## Running Ludwig train from command line

```bash
make train-ludwig  # this runs ludwig experiment --dataset data/neo.csv --config config.yaml
```

## Ludwig AutoML

Ludwig AutoML takes a dataset, the target column, and a time budget, and returns a trained Ludwig model.
Ludwig AutoML is currently experimental and is focused on tabular datasets.


[Documentation](https://ludwig-ai.github.io/ludwig-docs/0.5/user_guide/automl/)

```bash
./run_automl_ludwig.py
```

## FLAML AutoML

flaml.AutoML is a class for task-oriented AutoML. It can be used as a scikit-learn style estimator with the standard fit and predict functions. 
The minimal inputs from users are the training data and the task type.

[Documentation](https://microsoft.github.io/FLAML/docs/Use-Cases/Task-Oriented-AutoML/)

```bash
./run_automl_flaml.py
```

## Citation

```
@misc{Molino2019,
  author = {Piero Molino and Yaroslav Dudin and Sai Sumanth Miryala},
  title = {Ludwig: a type-based declarative deep learning toolbox},
  year = {2019},
  eprint = {arXiv:1909.07930},
}

@inproceedings{wang2021flaml,
    title={FLAML: A Fast and Lightweight AutoML Library},
    author={Chi Wang and Qingyun Wu and Markus Weimer and Erkang Zhu},
    year={2021},
    booktitle={MLSys},
}
```
