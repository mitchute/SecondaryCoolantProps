# Secondary Coolant Props

This repo contains some fluid property routines for secondary coolants. It is based on the correlations developed by Åke Melinder, 2010 "Properties of Secondary Working Fluids for Indirect Systems" 2nd ed., International Institute of Refrigeration.

This is intended to be a lightweight library that can be easily imported into any other Python tool, with no bulky dependencies.

## Code Quality

[![Flake8](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/flake8.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/flake8.yml)
[![Tests](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/tests.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/tests.yml)

Code is checked for style and tests executed by GitHub Actions.

## Documentation

[![Documentation Status](https://readthedocs.org/projects/secondarycoolantprops/badge/?version=latest)](https://secondarycoolantprops.readthedocs.io/en/latest/?badge=latest)

Docs are built from Sphinx on ReadTheDocs.org and are available at https://secondarycoolantprops.readthedocs.io/en/latest/

## Releases

[![PyPIRelease](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/release.yml/badge.svg)](https://github.com/mitchute/SecondaryCoolantProps/actions/workflows/release.yml)

When a release is tagged, a GitHub Action workflow will create a Python wheel and upload it to the PyPi server.

To install into an existing Python environment, execute `pip install SecondaryCoolantProps`

Project page: https://pypi.org/project/SecondaryCoolantProps/
