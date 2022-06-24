# Ludwig AutoML

Auto ML solution using [Ludwig](https://ludwig-ai.github.io/ludwig-docs/0.5/index.html),
a declarative deep learning framework that allows users to train, evaluate, and deploy models without the need to write code.


## Dataset

[NASA - Nearest Earth Objects](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects?datasetId=2272878&sortBy=voteCount&select=neo.csv)

>There is an infinite number of objects in the outer space. Some of them are closer than we think. Even though we might think that a distance of 70,000 Km can not potentially harm us, but at an astronomical scale, this is a very small distance and can disrupt many natural phenomena. These objects/asteroids can thus prove to be harmful. Hence, it is wise to know what is surrounding us and what can harm us amongst those. Thus, this dataset compiles the list of NASA certified asteroids that are classified as the nearest earth object.

## Development 

Creating virtual environment:

 1. ```python3 -m venv venv```
 2.  (On Unix or MacOS) ```source venv/bin/activate```

Contributing guidelines:

Run ```make all``` before pushing code.

## Running from command line

```bash
ludwig experiment --dataset data/neo.csv --config config.yaml
```
## Citation

```
@misc{Molino2019,
  author = {Piero Molino and Yaroslav Dudin and Sai Sumanth Miryala},
  title = {Ludwig: a type-based declarative deep learning toolbox},
  year = {2019},
  eprint = {arXiv:1909.07930},
}
```