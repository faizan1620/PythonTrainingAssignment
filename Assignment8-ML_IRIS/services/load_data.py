from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np


def load_iris_data():
    iris = load_iris()
    # Create a dataframe
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df['target'] = iris.target
    x = iris.data
    df.sample(4)
    return x,df,iris