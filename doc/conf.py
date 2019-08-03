import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'pyepgdb'
copyright = '2019, Joseph Lansdowne'
author = 'Joseph Lansdowne'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'haiku'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx'
]
nitpicky = True

autodoc_default_options = {
    'member-order': 'bysource',
    'members': True,
    'show-inheritance': True,
    'undoc-members': True,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
