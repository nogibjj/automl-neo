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


### Results

```json
            "eval_stats": {
                "combined": {
                    "loss": 0.16034649312496185
                },
                "hazardous": {
                    "accuracy": 0.9335024356842041,
                    "average_precision_macro": 0.6834651266845658,
                    "average_precision_micro": 0.6834651266845658,
                    "average_precision_samples": 0.6834651266845658,
                    "confusion_matrix": [
                        [
                            7915,
                            261
                        ],
                        [
                            342,
                            550
                        ]
                    ],
                    "loss": 0.16034649312496185,
                    "overall_stats": {
                        "avg_f1_score_macro": 0.8046122551263251,
                        "avg_f1_score_micro": 0.9335024261138067,
                        "avg_f1_score_weighted": 0.9320848967383845,
                        "avg_precision_macro": 0.8183778453793344,
                        "avg_precision_micro": 0.9335024261138067,
                        "avg_precision_weighted": 0.9335024261138067,
                        "avg_recall_macro": 0.7923346138320184,
                        "avg_recall_micro": 0.9335024261138067,
                        "avg_recall_weighted": 0.9335024261138067,
                        "kappa_score": 0.6093161036240407,
                        "token_accuracy": 0.9335024261138067
                    }
```

## FLAML AutoML

flaml.AutoML is a class for task-oriented AutoML. It can be used as a scikit-learn style estimator with the standard fit and predict functions. 
The minimal inputs from users are the training data and the task type.

[Documentation](https://microsoft.github.io/FLAML/docs/Use-Cases/Task-Oriented-AutoML/)

```bash
./run_automl_flaml.py
```

### Results

```bash
[flaml.automl: 07-05 16:11:47] {3342} INFO - retrained model: LGBMClassifier(colsample_bytree=0.3798570169670106,
               learning_rate=0.298364626315126, max_bin=1023,
               min_child_samples=8, n_estimators=1208, num_leaves=30,
               reg_alpha=0.010349130059024369, reg_lambda=0.04926637721736125,
               verbose=-1)
[flaml.automl: 07-05 16:11:47] {2636} INFO - fit succeeded
[flaml.automl: 07-05 16:11:47] {2638} INFO - Time taken to find the best model: 109.54706311225891
[flaml.automl: 07-05 16:11:47] {2652} WARNING - Time taken to find the best model is 91% of the provided time budget and not all estimators' hyperparameter search converged. Consider increasing the time budget.
Best ML leaner: lgbm
Best hyperparmeter config: {'n_estimators': 1208, 'num_leaves': 30, 'min_child_samples': 8, 'learning_rate': 0.298364626315126, 'log_max_bin': 10, 'colsample_bytree': 0.3798570169670106, 'reg_alpha': 0.010349130059024369, 'reg_lambda': 0.04926637721736125, 'FLAML_sample_size': 61314}
Best accuracy on validation data: 0.9745
Training duration of best run: 5.355 s
```

## Deepchecks Data Integrity Check

>Deepchecks is the leading tool for testing and for validating your machine learning models and data, and it enables doing so with minimal effort. Deepchecks accompanies you through various validation and testing needs such as verifying your data’s integrity, inspecting its distributions, 
> validating data splits, evaluating your model and comparing between different models.

[Docs](https://docs.deepchecks.com/)

As part of this project, we run the Data Integrity Suite composed of various checks such as: 
Mixed Nulls, Is Single Value, Outlier Sample Detection, etc.

```
pytest test_data_deepchecks.py
```
**OR**
```bash
make test
```

<img width="1060" alt="image" src="https://user-images.githubusercontent.com/12115186/177414711-1c948bb7-3f69-4d88-b440-b045e64e3b2e.png">

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
