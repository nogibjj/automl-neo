from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity
import pandas as pd

# Reference: https://docs.deepchecks.com/stable/user-guide/tabular/auto_tutorials/plot_quick_data_integrity.html
def test_data_integrity():
    # The label can be passed as a column name or a separate pd.Series / pd.DataFrame
    df = pd.read_csv("data/neo.csv")
    ds = Dataset(df, label="hazardous")
    # Run Suite
    integ_suite = data_integrity().remove(0)
    suite_result = integ_suite.run(ds)
    # Note: the result can be saved as html using suite_result.save_as_html()
    # or exported to json using suite_result.to_json()
    suite_result.save_as_html(file="deepchecks.html")
    assert len(suite_result.get_not_passed_checks()) == 0
