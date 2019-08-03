import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'pyepgdb'
copyright = '2019, Joseph Lansdowne'
author = 'Joseph Lansdowne'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'haiku'

autodoc_default_options = {
    'member-order': 'bysource',
    'members': True,
    'show-inheritance': True,
    'undoc-members': True,
}
