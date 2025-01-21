# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import importlib.metadata

from pathlib import Path
from sys import path

root_dir = Path(__file__).parent.parent.resolve()
path.insert(0, str(root_dir))

import datetime

project = 'SecondaryCoolantProps'
copyright = f'{datetime.date.today().year}, Mitchell, M.; Lee, E.'
author = 'Matt Mitchell, Edwin Lee'
release = importlib.metadata.version("SecondaryCoolantProps")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
