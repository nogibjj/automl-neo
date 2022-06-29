#!/usr/bin/env python3

import pprint
import pandas as pd
from ludwig.automl import auto_train

# Reading the csv file and storing it in a dataframe.
inputdf = pd.read_csv("data/neo.csv")

# Training the model.
# from ludwig.api import LudwigModel
# ludwig_model = LudwigModel(config="config.yaml")
# train_status = ludwig_model.train(dataset=inputdf)

# Printing the training status.
# pprint.pprint(train_status)

auto_train_results = auto_train(
    dataset=inputdf, target="hazardous", time_limit_s=120, tune_for_memory=True
)

pprint.pprint(auto_train_results)
