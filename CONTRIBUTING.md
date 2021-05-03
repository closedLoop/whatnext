# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Run all `pre-commit-hooks` defined below
2. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
3. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
4. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
5. You may merge the Pull Request in once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team via twitter [@seankruzel](https://twitter.com/seankruzel). All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/



# Code Quality Checks (pre-commit hooks)

```
pre-commit install
```

Below are details on many of the additional checks we could / should run

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
radon cc -nas --min=B -e="venv" raw ar_analysis/

# Maintainability
radon mi  -e="venv" raw /whatnext

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
