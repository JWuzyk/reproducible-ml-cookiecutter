# What is this for?

This folder should be used to store configuration files used by Kedro or by separate tools. A specific environment can be activated by setting the the `KEDRO_ENV` environment variable. If `KEDRO_ENV` is not set, `local` is used. Values are loaded from the active environment first and if not found there, loaded from `base`.

## Base configuration

The `base` folder is for non-sensitive configuration shared by all environments. Repetative configurations can be set here via templates and filled with variables from globals.yml.

WARNING: Please do not put access credentials in the base configuration folder.

## Local configuration

The `local` folder is for configuration and credentials specific to the local computer. Sensitive credentials should be kept here and will be git-ignored by default.

> *Note:* Please do not check in any local configuration to version control.

## Test configuration

The `test` folder is for configuration to be used by tests both locally and during CI.

## CI configuration

The `ci` folder is for configuration to be used when running the pipeline during CI/CD, for example during a train step.
