"""Test that the pipeline runs."""
from pathlib import Path

from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession


def test_train_pipeline() -> None:
    """Test that pipeline runs."""
    configure_project("{{ cookiecutter.package_name|slugify|replace("-", "_") }}_pipelines")

    with KedroSession.create(
        project_path=str(Path(__file__).parents[1]), save_on_close=False, env="test"
    ) as session:
        session.run()
