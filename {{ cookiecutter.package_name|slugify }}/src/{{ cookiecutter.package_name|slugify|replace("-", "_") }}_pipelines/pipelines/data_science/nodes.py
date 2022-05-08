"""Example code for the nodes in the example pipeline.

This code is meant just for illustrating basic Kedro features. Delete
this when you start working on your own Kedro project.
"""
import logging
from typing import Any, Dict

import numpy as np
import pandas as pd


def train_model(
    train_x: pd.DataFrame, train_y: pd.DataFrame, parameters: Dict[str, Any]
) -> np.ndarray:  # type: ignore[type-arg]
    """Node for training a simple multi-class logistic regression model.

    The number of training iterations as well as the learning rate are
    taken from conf/{env}/parameters.yml. All of the data as well as
    the parameters will be provided to this function at the time of
    execution.

    Parameters
    ----------
    train_x : pd.DataFrame
        Training input dataframe
    train_y : pd.DataFrame
        Training target dataframe
    parameters : Dict[str, Any]
        example_num_train_iter: int - number of iterations to train for
        example_num_train_iter: float - learning rate

    Returns
    -------
    np.ndarray
        Trained model weights
    """
    num_iter = parameters["example_num_train_iter"]
    lr = parameters["example_learning_rate"]
    x = train_x.to_numpy()
    y = train_y.to_numpy()

    # Add bias to the features
    bias = np.ones((x.shape[0], 1))
    x = np.concatenate((bias, x), axis=1)

    weights = []
    # Train one model for each class in Y
    for k in range(y.shape[1]):
        # Initialise weights
        theta = np.zeros(x.shape[1])
        _y = y[:, k]
        for _ in range(num_iter):
            z = np.dot(x, theta)
            h = _sigmoid(z)
            gradient = np.dot(x.T, (h - _y)) / _y.size
            theta -= lr * gradient
        # Save the weights for each model
        weights.append(theta)

    # Return a joint multi-class model with weights for all classes
    return np.vstack(weights).transpose()


def predict(model: np.ndarray, test_x: pd.DataFrame) -> np.ndarray:  # type: ignore[type-arg]
    """Node for making predictions given a pre-trained model and a test set.

    Parameters
    ----------
    model : np.ndarray
        Model weights
    test_x : pd.DataFrame
        Test dataframe values

    Returns
    -------
    np.ndarray
        Test dataframe predictions
    """
    x = test_x.to_numpy()

    # Add bias to the features
    bias = np.ones((x.shape[0], 1))
    x = np.concatenate((bias, x), axis=1)

    # Predict "probabilities" for each class
    result = _sigmoid(np.dot(x, model))

    # Return the index of the class with max probability for all samples
    return np.argmax(result, axis=1)  # type: ignore[no-any-return]


def report_accuracy(predictions: np.ndarray, test_y: pd.DataFrame) -> Dict[str, float]:  # type: ignore[type-arg]
    """Node for reporting the accuracy of the predictions performed by the previous node.

    Parameters
    ----------
    predictions : np.ndarray
        Test data model predictions
    test_y : pd.DataFrame
        Test data target labels

    Returns
    -------
    Dict[str, float]
        Model metrics:
            - accuracy : float
    """
    # Get true class index
    target = np.argmax(test_y.to_numpy(), axis=1)
    # Calculate accuracy of predictions
    accuracy = np.sum(predictions == target) / target.shape[0]
    # Log the accuracy of the model
    log = logging.getLogger(__name__)
    log.info("Model accuracy on test set: %0.2f%%", accuracy * 100)
    return {"accuracy": accuracy}


def _sigmoid(z: float) -> np.float32:
    """Sigmoid function used by the training and the scoring nodes.

    Parameters
    ----------
    z : float
        input value

    Returns
    -------
    float
        Value after applying sigmoid function.
    """
    return 1 / (1 + np.exp(-z))  # type: ignore[no-any-return]
