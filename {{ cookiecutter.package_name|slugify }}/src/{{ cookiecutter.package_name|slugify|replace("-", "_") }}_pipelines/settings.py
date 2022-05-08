"""Project settings.

There is no need to edit this file unless you want to change values
from the Kedro defaults. For further information, including these default values, see
https://kedro.readthedocs.io/en/stable/kedro_project_setup/settings.html.
"""
import os
from pathlib import Path

from kedro.config import ConfigLoader, TemplatedConfigLoader
from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore

# Super hacky fix: See https://github.com/kedro-org/kedro/issues/1402
ConfigLoader.__subclasses__ = lambda: [TemplatedConfigLoader]  # type: ignore[assignment, list-item]
CONFIG_LOADER_CLASS = TemplatedConfigLoader
CONFIG_LOADER_ARGS = {"globals_pattern": "*globals.yml", "default_run_env": "local"}

data_folder = f'data/{os.environ.get("KEDRO_ENV")}' if os.environ.get("KEDRO_ENV") else "data/local"
SESSION_STORE_CLASS = SQLiteStore
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / data_folder / "08_reporting")}
