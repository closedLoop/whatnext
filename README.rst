
.. image:: https://circleci.com/gh/AstrocyteResearch/whatnext/tree/master.svg?style=shield
    :target: https://circleci.com/gh/AstrocyteResearch/whatnext/tree/master

.. image:: https://codecov.io/gh/AstrocyteResearch/whatnext/branch/master/graph/badge.svg?token=6NVZUGMEZ8
  :target: https://codecov.io/gh/AstrocyteResearch/whatnext

.. image:: https://img.shields.io/pypi/v/whatnext.svg
    :target: https://pypi.python.org/pypi/whatnext

.. image:: https://img.shields.io/pypi/l/whatnext.svg
    :target: https://pypi.python.org/pypi/whatnext

.. image:: https://img.shields.io/pypi/pyversions/whatnext.svg
    :target: https://pypi.python.org/pypi/whatnext

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/AstrocyteResearch/whatnext

------


.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/AstrocyteResearch/whatnext

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/AstrocyteResearch/whatnext/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/AstrocyteResearch/whatnext/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/whatnext#files


whatnext
==============================================================================
For devs whose heads overflow with tasks and need a way to prioritize


.. _install:

Install
------------------------------------------------------------------------------

``whatnext`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install whatnext

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade whatnext


Usage
------------------------------------------------------------------------------

.. code-block:: python3

    from whatnext import WhatNextServer
    api = WhatNextServer(api_key="ENTER_YOUR_KEY")
    api.serve()


Development
------------------------------------------------------------------------------

.. code-block:: console

    $ # create venv
    $ virtualenv -p python3.8 venv

    $ # Install
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ pip install -e .


Test
------------------------------------------------------------------------------

.. code-block:: console

    $ python ./tests/all.py



Build
------------------------------------------------------------------------------

.. code-block:: console

    $ python3 -m pip install --user --upgrade setuptools wheel
    $ python3 setup.py sdist bdist_wheel


Deploy
------------------------------------------------------------------------------

.. code-block:: console

    $ # Update coverage
    $ coverage xml
    $ bash <(curl -s https://codecov.io/bash)
    $ # Build
    $ rm ./dist/whatnext-* || python3 setup.py sdist bdist_wheel
    $ # Upload to pypi
    $ python3 -m twine upload dist/*
