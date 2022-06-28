import sklearn.metrics
import pandas as pd
from flaml import AutoML

input_df = pd.read_csv("data/neo.csv")
X = input_df.drop(["hazardous"], axis=1)
y = input_df["hazardous"]  # pylint: disable=E1136

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, random_state=1
)

automl = AutoML()

settings = {
    "time_budget": 120,  # total running time in seconds
    "metric": "accuracy",  # can be: 'r2', 'rmse', 'mae', 'mse', 'accuracy', 'roc_auc', 'roc_auc_ovr',
    # 'roc_auc_ovo', 'log_loss', 'mape', 'f1', 'ap', 'ndcg', 'micro_f1', 'macro_f1'
    "task": "classification",  # task type
    "seed": 7654321,  # random seed
}

automl.fit(X_train=X_train, y_train=y_train, **settings)

# retrieve best config and best learner
print("Best ML leaner:", automl.best_estimator)
print("Best hyperparmeter config:", automl.best_config)
print("Best accuracy on validation data: {0:.4g}".format(1 - automl.best_loss))
print(
    "Training duration of best run: {0:.4g} s".format(
        automl.best_config_train_time
    )
)
