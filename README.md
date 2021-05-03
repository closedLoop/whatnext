
[![closedloop](https://circleci.com/gh/closedLoop/whatnext.svg?style=shield)](https://circleci.com/gh/closedLoop/whatnext)

[![codecov](https://codecov.io/gh/closedLoop/whatnext/branch/main/graph/badge.svg?token=ZZH9IU8TDF)](https://codecov.io/gh/closedLoop/whatnext)

[![pypi](https://img.shields.io/pypi/v/whatnext.svg)](https://pypi.python.org/pypi/whatnext)

[![versions](https://img.shields.io/pypi/pyversions/whatnext.svg)](https://pypi.python.org/pypi/whatnext)

[![starme](https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social)](https://github.com/closedloop/whatnext)

------

[![GitHub](https://img.shields.io/badge/Link-GitHub-blue.svg)](https://github.com/closedloop/whatnext)
[![issues](https://img.shields.io/badge/Link-Submit_Issue-blue.svg)](https://github.com/closedloop/whatnext/issues)

```
>>                ___          ___     ___
>> |  | |__|  /\   |     |\ | |__  \_/  |   ___\
>> |/\| |  | /~~\  |     | \| |___ / \  |      /
>>
```
# Whatnext

For founders & devs whose heads overflow with tasks and dependencies.

We use the commandline to keep you in the flow of your work and Directed
Acyclic Graphs to organize your tasks.

## Getting Started

```bash
$ pip install whatnext

$ whatnext add "create your first task & grab coffee! -> create your second"

$ whatnext task  # Shows grab coffee

```

The syntax is simple:
 * `->` break text into subtasks and define dependencies
 * `&` within a task description define two separate and independent tasks
 * `!!!` the number of exclamation points in a task defines its importance
 * `#hashtags`, `@mentions` and `urls` are defined as special types to be used for filtering
 * dates within the string will be parsed as due dates

### Prerequisites

 * python3
 * pip


## Examples

TODO


## Running the tests

### Installing

``whatnext`` is released on PyPI, so all you need is:

```
$ pip install whatnext
```

To upgrade to latest version:
```
$ pip install --upgrade whatnext
```

### Configure Dev environment

Create virtual environment and install requirements
```
$ # create venv
$ virtualenv -p python3.8 venv

$ # Install requirements
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```

Install in editable mode
```
$ pip install -e .
```

Or Build the wheel
```
$ python -m pip install --user --upgrade setuptools wheel
$ python setup.py sdist bdist_wheel
```

Install the pre-commit hooks
```
$ pre-commit install
```

**Optional** set graph storage location

```
$ whatnext set-storage /local/data/
```
Or set it directly with environment variables

```
$ export WN_STORAGE_DIR=/local/data/
```

If installed properly the following will show

```
$ whatnext show

>>                ___          ___     ___
>> |  | |__|  /\   |     |\ | |__  \_/  |   ___\
>> |/\| |  | /~~\  |     | \| |___ / \  |      /
>>
```

## Running the tests

We use `pytest` to run all of our tests and coverage.  We use `unittest` to implement the individual tests.

```
# In your dev environment configured above
$ pip install -r requirements-test.txt

$ python ./tests/all.py
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Coding style is enforced using the pre-commit-hooks defined here `.pre-commit-config.yaml` and more details are available in [CONTRIBUTING.md](CONTRIBUTING.md)

* [black](https://github.com/psf/black): configuration is here [pyproject.toml](pyproject.toml)
* [flake8](https://github.com/pycqa/flake8): configuration is here [.flake8](.flake8)


```
Give an example
```

## Deployment

Deploy to Pypi
```
$ # Update coverage
$ coverage xml
$ bash <(curl -s https://codecov.io/bash)

$ # Build
$ rm ./dist/whatnext-* || python3 setup.py sdist bdist_wheel

$ # Upload to pypi
$ python3 -m twine upload dist/*
```

## Built With

* [typer](https://github.com/tiangolo/typer) - for the CLI
* [networkx](https://github.com/networkx/networkx) - stores the graph representation
* [pydantic](https://github.com/samuelcolvin/pydantic) - the Task and TimeLog datamodel
* [dateparser](https://github.com/scrapinghub/dateparser) - parses due dates in the tasks
* [tabulate](https://github.com/astanin/python-tabulate) - show the tasks in the terminal

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/closedloop/whatnext/tags).

## Authors

* **Sean Kruzel** - *Initial work* - [PurpleBooth](https://github.com/closedloop)

See also the list of [contributors](https://github.com/closedloop/whatnext/contributors) who participated in this project.

## License

This project is licensed under the Apache 2.0 with Commons Clause - see the [LICENSE.txt](LICENSE.txt) file for details
