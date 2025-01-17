"""Example code for the nodes in the example pipeline.

This code is meant just for illustrating basic Kedro features. Delete
this when you start working on your own Kedro project.
"""
from kedro.pipeline import Pipeline, node

from .nodes import split_data


def create_pipeline() -> Pipeline:
    """Create data engineering pipeline.

    Returns
    -------
    Pipeline
        Created pipeline.
    """
    return Pipeline(
        [
            node(
                split_data,
                ["example_iris_data", "params:example_test_data_ratio"],
                {
                    "train_x": "example_train_x",
                    "train_y": "example_train_y",
                    "test_x": "example_test_x",
                    "test_y": "example_test_y",
                },
                name="split",
            )
        ]
    )
