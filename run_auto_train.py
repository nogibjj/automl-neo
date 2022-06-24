import pprint

import pandas as pd
from ludwig.automl import auto_train

input_df = pd.read_csv('data/neo.csv')

auto_train_results = auto_train(
    dataset=input_df,
    target='hazardous',
    time_limit_s=120,
    tune_for_memory=False
)

pprint.pprint(auto_train_results)