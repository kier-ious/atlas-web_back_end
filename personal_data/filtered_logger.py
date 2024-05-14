#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""

import re


def filter_datum(fields, redaction, message,separator):
    pattern = '|'.join(fields)
    return re.sub(f'({pattern})=[^{separator}]*', f'\\1={redaction}', message)
