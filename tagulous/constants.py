"""
Tagulous constants
"""
from __future__ import unicode_literals

import six


# Prefix for all models auto-generated by Tagulous
MODEL_PREFIX = 'Tagulous'

# Constants to improve code legibility
COMMA = ','
SPACE = ' '
QUOTE = '"'
DOUBLE_QUOTE = QUOTE + QUOTE
TREE = '/'

# Default model TagField options
OPTION_DEFAULTS = {
    'initial':          '',
    'protect_initial':  True,
    'protect_all':      False,
    'case_sensitive':   False,
    'force_lowercase':  False,
    'max_count':        0,
    'space_delimiter':  True,
    'tree':             False,
    'autocomplete_initial': False,
    'autocomplete_view':    '',
    'autocomplete_limit':   100,
    'autocomplete_settings':    None,
    'get_absolute_url':         None,
    'verbose_name_singular':    None,
    'verbose_name_plural':      None,
}

# List of model TagField options which are relevant to form fields
FORM_OPTIONS = [
    'case_sensitive',
    'force_lowercase',
    'max_count',
    'space_delimiter',
    'tree',
    'autocomplete_limit',
    'autocomplete_settings'
]
