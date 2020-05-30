# -*- coding: utf-8 -*-
"""A pytest plugin for use with homeassistant custom components.

This plugin provides pytest fixtures and common testing utils to make testing custom
components easier.  The fixtures and test utils come from the homeassistant core project.
"""
import pytest

from .fixtures import aioclient_mock, hass, hass_storage
