====================
pytest-homeassistant
====================

.. image:: https://img.shields.io/pypi/v/pytest-homeassistant.svg
    :target: https://pypi.org/project/pytest-homeassistant
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-homeassistant.svg
    :target: https://pypi.org/project/pytest-homeassistant
    :alt: Python versions

A pytest plugin for use with homeassistant custom components.

----

This `pytest`_ plugin provides several pytest fixtures and utils to make testing
`homeassistant`_ custom components easier.

The plugin allows you to use a subset of fixtures and helpers from the
`homeassistant`_ test code to allow you to test your own custom components.


Features
--------

Fixtures
########

* `hass` - Used to mock a hass instance.  This is primarily useful in testing your
  `config_flow` code.  Examples of it's usage can be found in the homeassistant
  tests. (`example <https://github.com/home-assistant/core/blob/dev/tests/components/hue/test_config_flow.py#L48>`_)
* `aioclient_mock` - Used to mock responses from `homeassistant.helpers.aiohttp_client.async_get_clientsession`
  in your test code. (`example test <https://github.com/home-assistant/core/blob/605b0ceb5fd50df938c19758e093c005ba9ddfe8/tests/components/alexa/test_state_report.py#L7>`_)

Helpers
#######

* `pytest_homeassistant.async_mock` - Contains all mock methods that can handle
  async calls.

.. code-block:: python

    from pytest_homeassistant.async_mock import AsyncMock, patch

    async def test_async_thing():
        with patch("mymodule.get_async_thing") as m_get_async_thing:
            m_get_async_thing.return_value = AsyncMock()
            await get_async_thing()

Requirements
------------

* homeassistant


Installation
------------

You can install "pytest-homeassistant" via `pip`_ from `PyPI`_::

    $ pip install pytest-homeassistant


Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-homeassistant" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/boralyl/pytest-homeassistant/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`homeassistant`: https://github.com/home-assistant/core
