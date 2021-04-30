
# Code Quality Checks (pre-commit hooks)


```
pre-commit install
```

```
repos:
 - repo: https://github.com/pre-commit/pre-commit-hooks
   rev: v2.5.0
   hooks:
   - id: double-quote-string-fixer
   - id: trailing-whitespace
   - id: end-of-file-fixer
   - id: mixed-line-ending
     args: ['--fix=lf']
   - id: check-added-large-files
     args: ['--maxkb=15000']
   - id: no-commit-to-branch
 - repo: https://github.com/PyCQA/isort
   rev: 5.6.4
   hooks:
   - id: isort
 - repo: https://github.com/ambv/black
   rev: 20.8b1
   hooks:
   - id: black
 - repo: https://github.com/myint/eradicate
   rev: v2.0.0
   hooks:
   - id: eradicate

 - repo: https://github.com/jendrikseipp/vulture
   rev: v2.1
   hooks:
   - id: vulture
```


## Generic Clean up code / file formats
 - repo: https://github.com/pre-commit/pre-commit-hooks
   rev: v2.5.0
   hooks:
   - id: trailing-whitespace
   - id: end-of-file-fixer
   - id: mixed-line-ending
     args: ['--fix=lf']
   - id: check-added-large-files
     args: ['--maxkb=15000']
   - id: no-commit-to-branch

## Clean up imports
 - repo: https://github.com/PyCQA/isort
   rev: 5.6.4
   hooks:
   - id: isort

## Code Formatting
 - repo: https://github.com/ambv/black
   rev: 20.8b1
   hooks:
   - id: black
 - repo: https://github.com/myint/eradicate


## Check Code Hints
https://github.com/python/mypy

## Security
https://github.com/PyCQA/bandit

After we know code is formatted, we can start pruning and checking things

## unused inports
https://github.com/PyCQA/pyflakes
https://gitlab.com/pycqa/flake8

## Code that cant be accessed anywhere
https://github.com/jendrikseipp/vulture

## Test Coverage
https://github.com/nedbat/coveragepy

## PEP8 Python formatting (more detailed than Black)
https://github.com/PyCQA/pycodestyle

```
pycodestyle --exclude="./profile_nbserver,portformer-scoring-venv,./ar_portformer/deprec_portformer.py" --max-line-length=88 --statistics --ignore=E741,E743,E203,E501,W503 --first  .
```

## Code complexity
https://github.com/rubik/radon

**requirements.txt**
```
pip install pre-commit-hooks==3.3.0
pip install isort==5.6.4
pip install black==20.8b1
pip install eradicate==2.0.0
pip install pyflakes==2.1.1
pip install vulture==2.1
pip install coverage==5.2
pip install pycodestyle==2.5.0
pip install mypy==0.790
pip install bandit==1.6.2
pip install radon==4.3.2
```

Running manually (without hooks)
```
# pre-commit-hooks
pre-commit run trailing-whitespace
pre-commit run end-of-file-fixer
pre-commit run mixed-line-ending
pre-commit run check-added-large-files
pre-commit run no-commit-to-branch

# TODO still runs on all subfolders
isort --only-modified ar_analysis/**/*.py

# Black - reads config from pyproject.toml
black .

# Remove Dead Code
eradicate --recursive --in-place ar_analysis/.

# Security Check
bandit -s B101 -r **/*.py

# MANUAL TASKS

# Remove Unused / Unreachable Code - reads config from pyproject.toml
vulture .

# TODO Code coverage

# Type Annovations
mypy --python-version 3.8 --strict

# Pyflakes - TODO only certain files
pyflakes

# Radon
# Complexity
radon cc -nas --min=B -e="portformer-scoring-venv" raw ar_analysis/
# Maintainability
radon mi  -e="portformer-scoring-venv" raw ar_breakpoint/

# Testing
<!-- https://stackoverflow.com/questions/59586334/python-pre-commit-unittest-skipped#59587876 -->

python -m unittest discover

    <!-- -   id: unittest
        name: unittest
        entry: python -m unittest discover
        language: python
        'types': [python]
        additional_dependencies: []
        pass_filenames: false -->
```
