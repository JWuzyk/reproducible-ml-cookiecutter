"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from {{ cookiecutter.package_name|slugify|replace("-", "_") }}_pipelines.pipelines import data_engineering as de
from {{ cookiecutter.package_name|slugify|replace("-", "_") }}_pipelines.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns
    -------
    Dict[str, Pipeline]
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_engineering_pipeline = de.create_pipeline()  # type: ignore[attr-defined]
    data_science_pipeline = ds.create_pipeline()  # type: ignore[attr-defined]

    return {
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline,
    }
