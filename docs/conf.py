# conf.py -- minimal, yet useful Sphinx config
import os
import sys
from datetime import datetime


# add project src to path so autodoc can find modules
sys.path.insert(0, os.path.abspath('../src'))


project = 'Example Project'
author = 'Your Name'
copyright = f"{datetime.now().year}, {author}"


extensions = [
'sphinx.ext.autodoc', # generate docs from docstrings
'sphinx.ext.napoleon', # Google/NumPy style docstrings
'sphinx.ext.viewcode', # link to source
'sphinx.ext.intersphinx',# link to other projects docs
'sphinx.ext.todo', # TODOs in docs
'sphinx.ext.mathjax', # render math with MathJax
'sphinx.ext.autosummary' # create autosummary pages
]


autosummary_generate = True


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'


# Intersphinx mapping (example)
intersphinx_mapping = {
'python': ('https://docs.python.org/3', None),
}


# Show TODOs in the output while developing
todo_include_todos = True


# Basic autodoc options
autodoc_member_order = 'bysource'
autodoc_default_options = {
'members': True,
'undoc-members': False,
'show-inheritance': True,
}