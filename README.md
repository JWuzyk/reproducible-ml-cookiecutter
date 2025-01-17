# Reproducible ML Cookiecutter

This project is a fork of [Poetry Cookiecutter](https://github.com/radix-ai/poetry-cookiecutter). The goal is to extend that project with an example of a well structured full reproducible ML model training pipeline. This is achieved by using Kedro, DVC and Gitlab-CI. For now this project only works on gitlab. 


## Using

<details open>
<summary>Setting up a new project with this template</summary>

1. Install [Cruft](https://cruft.github.io/cruft/) in your Python environment with:
   ```sh
   pip install cruft
   ```
2. Create a new repository on gitlab and clone it locally.
3. In the repository's parent directory, run:
   ```sh
   cruft create -f git@github.com:JWuzyk/reproducible-ml-cookiecutter.git
   ```
4. [Optional] To use the setup script: This will create an azure blob storage as dvc backing store and set the variables needed in gitlab for the training pipeline to work.
   - Create a Gitlab access token with API rights.
   - Fill in the variables in setup/script.sh and run the script.

</details>

<details open>
<summary>Updating your project with the latest template</summary>

1. Run `cruft check` to check for updates.
2. Run `cruft update` to update to the latest scaffolding.
3. Address failed merges in any `.rej` files.

</details>

## Features

### NEW
- Keep track of data versions and share data easily using [DVC](https://dvc.org/) with an azure blob storage backing store.
- Structure data science code following good software engineering practices using [kedro](https://kedro.readthedocs.io/en/stable/).
- Experiment locally and train final models remotely using [gitlab-ci](https://docs.gitlab.com/ee/ci/), making every model tied to a commit and completely reporducible.
- Compare model performance using [kedro-viz](https://kedro.readthedocs.io/en/0.17.4/03_tutorial/06_visualise_pipeline.html).
- A fully functioning basic example demonstrating how all these features work together.
 ### Poetry Cookiecutter
- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/remote/containers) and PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort)
- ✅ Code linting with [pre-commit](https://pre-commit.com/): [bandit](https://github.com/PyCQA/bandit), [darglint](https://github.com/terrencepreilly/darglint), [flake8](https://github.com/PyCQA/flake8), [mypy](https://github.com/python/mypy), [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks), [pydocstyle](https://github.com/PyCQA/pydocstyle), [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks), [pyupgrade](https://github.com/asottile/pyupgrade), [safety](https://github.com/pyupio/safety), and [shellcheck](https://github.com/koalaman/shellcheck)
- 🏷 Follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions) or [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding upgrades with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Automated dependency updating with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
