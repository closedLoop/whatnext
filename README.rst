

.. image:: https://circleci.com/gh/closedLoop/whatnext.svg?style=shield
   :target: https://circleci.com/gh/closedLoop/whatnext
   :alt: closedloop



.. image:: https://codecov.io/gh/closedLoop/whatnext/branch/main/graph/badge.svg?token=ZZH9IU8TDF
   :target: https://codecov.io/gh/closedLoop/whatnext
   :alt: codecov



.. image:: https://img.shields.io/pypi/v/whatnext.svg
   :target: https://pypi.python.org/pypi/whatnext
   :alt: pypi



.. image:: https://img.shields.io/pypi/pyversions/whatnext.svg
   :target: https://pypi.python.org/pypi/whatnext
   :alt: versions



.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
   :target: https://github.com/closedloop/whatnext
   :alt: starme


----


.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
   :target: https://github.com/closedloop/whatnext
   :alt: GitHub


.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
   :target: https://github.com/closedloop/whatnext/issues
   :alt: issues


.. code-block::

    >>                ___          ___     ___
    >> |  | |__|  /\   |     |\ | |__  \_/  |   ___\
    >> |/\| |  | /~~\  |     | \| |___ / \  |      /
    >>

Whatnext
========

For founders & devs whose heads overflow with tasks and dependencies.

We use the commandline to keep you in the flow of your work and Directed
Acyclic Graphs to organize your tasks.

Getting Started
---------------

.. code-block:: bash

   $ pip install whatnext

   $ whatnext add "create your first task & grab coffee! -> create your second"

   $ whatnext task  # Shows grab coffee

The syntax is simple:


* ``->`` break text into subtasks and define dependencies
* ``&`` within a task description define two separate and independent tasks
* ``!!!`` the number of exclamation points in a task defines its importance
* ``#hashtags``\ , ``@mentions`` and ``urls`` are defined as special types to be used for filtering
* dates within the string will be parsed as due dates

Prerequisites
^^^^^^^^^^^^^


* python3
* pip

Examples
--------

TODO

Running the tests
-----------------

Installing
^^^^^^^^^^

``whatnext`` is released on PyPI, so all you need is:

.. code-block::

   $ pip install whatnext

To upgrade to latest version:

.. code-block::

   $ pip install --upgrade whatnext

Configure Dev environment
^^^^^^^^^^^^^^^^^^^^^^^^^

Create virtual environment and install requirements

.. code-block::

   $ # create venv
   $ virtualenv -p python3.8 venv

   $ # Install requirements
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   $ pip install -r requirements-dev.txt

Install in editable mode

.. code-block::

   $ pip install -e .

Or Build the wheel

.. code-block::

   $ python -m pip install --user --upgrade setuptools wheel
   $ python setup.py sdist bdist_wheel

Install the pre-commit hooks

.. code-block::

   $ pre-commit install

**Optional** set graph storage location

.. code-block::

   $ whatnext set-storage /local/data/

Or set it directly with environment variables

.. code-block::

   $ export WN_STORAGE_DIR=/local/data/

If installed properly the following will show

.. code-block::

    $ whatnext show

    >>                ___          ___     ___
    >> |  | |__|  /\   |     |\ | |__  \_/  |   ___\
    >> |/\| |  | /~~\  |     | \| |___ / \  |      /
    >>

Running the tests
-----------------

We use ``pytest`` to run all of our tests and coverage.  We use ``unittest`` to implement the individual tests.

.. code-block::

   # In your dev environment configured above
   $ pip install -r requirements-test.txt

   $ python ./tests/all.py

Break down into end to end tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explain what these tests test and why

.. code-block::

   Give an example

And coding style tests
^^^^^^^^^^^^^^^^^^^^^^

Coding style is enforced using the pre-commit-hooks defined here ``.pre-commit-config.yaml`` and more details are available in `CONTRIBUTING.md <CONTRIBUTING.md>`_


* `black <https://github.com/psf/black>`_\ : configuration is here `pyproject.toml <pyproject.toml>`_
* `flake8 <https://github.com/pycqa/flake8>`_\ : configuration is here `.flake8 <.flake8>`_

.. code-block::

   Give an example

Deployment
----------

Deploy to Pypi

.. code-block::

   $ # Update coverage
   $ coverage xml
   $ bash <(curl -s https://codecov.io/bash)

   $ # Build
   $ rm ./dist/whatnext-* || python3 setup.py sdist bdist_wheel

   $ # Upload to pypi
   $ python3 -m twine upload dist/*

Built With
----------


* `typer <https://github.com/tiangolo/typer>`_ - for the CLI
* `networkx <https://github.com/networkx/networkx>`_ - stores the graph representation
* `pydantic <https://github.com/samuelcolvin/pydantic>`_ - the Task and TimeLog datamodel
* `dateparser <https://github.com/scrapinghub/dateparser>`_ - parses due dates in the tasks
* `tabulate <https://github.com/astanin/python-tabulate>`_ - show the tasks in the terminal

Contributing
------------

Please read `CONTRIBUTING.md <CONTRIBUTING.md>`_ for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
----------

We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/closedloop/whatnext/tags>`_.

Authors
-------


* **Sean Kruzel** - *Initial work* - `PurpleBooth <https://github.com/closedloop>`_

See also the list of `contributors <https://github.com/closedloop/whatnext/contributors>`_ who participated in this project.

License
-------

This project is licensed under the Apache 2.0 with Commons Clause - see the `LICENSE.txt <LICENSE.txt>`_ file for details
