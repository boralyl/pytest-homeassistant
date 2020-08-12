#!/usr/bin/env python

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


REQUIREMENTS = [
    "homeassistant",
    "asynctest>=0.13.0,<0.14.0",
    "astroid>=2.3.3,<2.5.0",
    "mock-open>=1.4.0,<2.0.0",
    "pytest-aiohttp>=0.3.0,<0.4.0",
    "pytest-timeout>=1.3.4,<2.0.0",
    "pytest>=5.4.0,<6.1.0",
    "requests_mock>=1.8.0,<2.0.0",
    "responses>=0.10.6,<0.11.0",
]

setup(
    name="pytest-homeassistant",
    version="0.1.3",
    author="Aaron Godfrey",
    maintainer="Aaron Godfrey",
    license="MIT",
    url="https://github.com/boralyl/pytest-homeassistant",
    description="A pytest plugin for use with homeassistant custom components.",
    long_description=read("README.rst"),
    packages=["pytest_homeassistant"],
    python_requires=">=3.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=REQUIREMENTS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["homeassistant = pytest_homeassistant.plugin"]},
)
