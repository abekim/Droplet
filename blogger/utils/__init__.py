"""
Basic utilites used across #dropplet.

Included in this module:
- slugify: return a unique string identifier given a BlogPost object.

author: @abekim
"""

# Slug regex rules
RULES = [
    ('\s+', '-'),
    ('[^\w\-]+', ''),
    ('\-\-+', '-'),
]

import re

def slugify(text=''):
    """
    Given a text, return the same string, modified by the following set of rules:
        - s/(.*)/\L1/: lower case the text
        - s/^\s+|\s+$//g: remove all leading and trailing whitespace
        - s/\s+/-/g: replace all whitespace to endash
        - s/[^\w\-]+//g: remove any non-word characters
        - s/\-\-+/-/g: replace all multiple endash with a single endash
    """
    if not text or type(text) is not str:
        # Log to the app or do something
        return ''

    text = text.lower().strip()
    for rule in RULES:
        text = re.sub(rule[0], rule[1], text)
    return text
