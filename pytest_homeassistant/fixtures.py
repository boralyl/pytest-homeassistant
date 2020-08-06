"""Fixtures provided by homeassistant.core"""
import asyncio

from homeassistant import runner
from homeassistant.exceptions import ServiceNotFound
import pytest

from .aiohttp_mock import mock_aiohttp_client

asyncio.set_event_loop_policy(runner.HassEventLoopPolicy(False))
# Disable fixtures overriding our beautiful policy
asyncio.set_event_loop_policy = lambda policy: None


@pytest.fixture
def hass_storage():
    """Fixture to mock storage."""
    # prevents circular dependency
    from .common import mock_storage

    with mock_storage() as stored_data:
        yield stored_data


@pytest.fixture
def hass(loop, hass_storage, request):
    """Fixture to provide a test instance of Home Assistant."""
    # prevents circular dependency
    from .common import async_test_home_assistant

    def exc_handle(loop, context):
        """Handle exceptions by rethrowing them, which will fail the test."""
        exceptions.append(context["exception"])
        orig_exception_handler(loop, context)

    exceptions = []
    hass = loop.run_until_complete(async_test_home_assistant(loop))
    orig_exception_handler = loop.get_exception_handler()
    loop.set_exception_handler(exc_handle)

    yield hass

    loop.run_until_complete(hass.async_stop(force=True))
    for ex in exceptions:
        if isinstance(ex, ServiceNotFound):
            continue
        raise ex


@pytest.fixture
def aioclient_mock():
    """Fixture to mock aioclient calls."""
    with mock_aiohttp_client() as mock_session:
        yield mock_session
