import pprint
from ludwig.api import LudwigModel
import pandas as pd

inputdf = pd.read_csv("data/neo.csv")

ludwig_model = LudwigModel(config="config.yaml")
train_status = ludwig_model.train(dataset=inputdf)

pprint.pprint(train_status)
