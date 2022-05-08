"""Example code for the nodes in the example pipeline.

This code is meant just for illustrating basic Kedro features. Delete
this when you start working on your own Kedro project.
"""
from typing import Dict

import pandas as pd


def split_data(data: pd.DataFrame, example_test_data_ratio: float) -> Dict[str, pd.DataFrame]:
    """Node for splitting the classical Iris data set into training and test sets.

    Test and train sets are each split into features and labels.
    The split ratio parameter is taken from conf/project/parameters.yml.
    The data and the parameters will be loaded and provided to your function
    automatically when the pipeline is executed and it is time to run this node.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataframe
    example_test_data_ratio : float
        Ratio used to split train and test data.

    Returns
    -------
    Dict[str, Any]
        train_x: pd.Dataframe - training dataset input features,
        train_y: pd.Dataframe - training dataset target labels,
        test_x: pd.Dataframe - test dataset input features,
        test_y: pd.Dataframe - test dataset target labels,
    """
    data.columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target",
    ]
    classes = sorted(data["target"].unique())
    # One-hot encoding for the target variable
    data = pd.get_dummies(data, columns=["target"], prefix="", prefix_sep="")

    # Shuffle all the data
    data = data.sample(frac=1).reset_index(drop=True)

    # Split to training and testing data
    n = data.shape[0]
    n_test = int(n * example_test_data_ratio)
    training_data = data.iloc[n_test:, :].reset_index(drop=True)
    test_data = data.iloc[:n_test, :].reset_index(drop=True)

    # Split the data to features and labels
    train_data_x = training_data.loc[:, "sepal_length":"petal_width"]  # type: ignore[misc]
    train_data_y = training_data[classes]
    test_data_x = test_data.loc[:, "sepal_length":"petal_width"]  # type: ignore[misc]
    test_data_y = test_data[classes]

    # When returning many variables, it is a good practice to give them names:
    return {
        "train_x": train_data_x,
        "train_y": train_data_y,
        "test_x": test_data_x,
        "test_y": test_data_y,
    }
