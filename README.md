# Secondary Coolant Props

This repo contains some fluid property routines for secondary coolants.
This is intended to be a very lightweight library that can be imported into any other Python tool very easily, with no bulky dependencies.

## Code Quality

[![Flake8](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/flake8.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/flake8.yml)
[![Tests](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/test.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/test.yml)

Code is checked for style and with unit tests by GitHub Actions using nosetests to sniff out the tests.

## Documentation

[![Sphinx docs to gh-pages](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/docs.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/docs.yml)
[![gh-pages](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/pages/pages-build-deployment)

Docs are built from Sphinx by GitHub Actions and followed up with a deployment to GH-Pages using Actions, available at https://mitchute.github.io/SecondaryCoolantProps/

## Releases

[![PyPIRelease](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/release.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/release.yml)

When a release is tagged, a GitHub Action workflow will create a Python wheel and upload it to the PyPi server.

To install into an existing Python environment, execute `pip install SecondaryCoolantProps`

Project page: https://pypi.org/project/SecondaryCoolantProps/
