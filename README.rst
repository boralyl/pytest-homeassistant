====================
pytest-homeassistant
====================

.. image:: https://img.shields.io/pypi/v/pytest-homeassistant.svg
    :target: https://pypi.org/project/pytest-homeassistant
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-homeassistant.svg
    :target: https://pypi.org/project/pytest-homeassistant
    :alt: Python versions

.. image:: https://img.shields.io/github/workflow/status/boralyl/pytest-homeassistant/Python%20package
    :alt: GitHub Workflow Status

A pytest plugin for use with Home Assistant custom components.

----

This `pytest`_ plugin provides several pytest fixtures and utils to make testing
`Home Assistant`_ custom components easier.

The plugin allows you to use a subset of fixtures and helpers from the
`Home Assistant`_ test code to allow you to test your own custom components.


Features
--------

Fixtures
########

* ``hass`` - Used to mock a hass instance.  This is primarily useful in testing your
  `config_flow` code.  Examples of it's usage can be found in the Home Assistant
  tests.

.. code-block:: python

    from custom_components.steam_wishlist import config_flow

    async def test_flow_init(hass):
        """Test the initial flow."""
        result = await hass.config_entries.flow.async_init(
            config_flow.DOMAIN, context={"source": "user"}
        )

        expected = {
            "data_schema": config_flow.DATA_SCHEMA,
            "description_placeholders": None,
            "errors": {},
            "flow_id": mock.ANY,
            "handler": "steam_wishlist",
            "step_id": "user",
            "type": "form",
        }
        assert expected == result

* ``aioclient_mock`` - Used to mock responses from `homeassistant.helpers.aiohttp_client.async_get_clientsession`
  in your test code.

You can find example usage of both of these fixtures in the `Home Assistant tests <https://github.com/home-assistant/core/tree/dev/tests>`_ directory.

Helpers
#######

* `pytest_homeassistant.async_mock` - Contains all mock methods that can handle
  async calls.

.. code-block:: python

    from pytest_homeassistant.async_mock import AsyncMock
    from custom_components.steam_wishlist import sensor_manager

    async def test_sensormanager_async_register_component(
        hass, coordinator_mock
    ):
    """Test that we add listeners and referesh data if all platforms were registered."""
        manager = sensor_manager.SensorManager(hass, url="http://fake.com")
        mock_async_add_entities = AsyncMock()
        await manager.async_register_component("sensor", mock_async_add_entities)

        assert mock_async_add_entities.called is True

Requirements
------------

* homeassistant


Installation
------------

You can install "pytest-homeassistant" via `pip`_ from `PyPI`_::

    $ pip install pytest-homeassistant


Contributing
------------
Contributions are very welcome.  I only incldued fixtures and test helpers that
were useful to me when testing my custom components.  If there are others that would
be useful to you, pull requests are welcome!

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-homeassistant" is free and open source software.


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
.. _`Home Assistant`: https://github.com/home-assistant/core
