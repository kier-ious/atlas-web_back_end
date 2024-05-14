#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""

import re
from typing import List
import logging


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """Obfuscates specified fields in a log msg

    Args:
        fields (list): a list of strings representing all fields to obfuscate
        redaction (str): a string representing by what the field will be
            obfuscated
        message (str): a string representing the log line
        separator (str): a string representing by which character is separating
            all fields in the log line (message)

    Returns:
        str: The log message w/ specified fields obfuscated
    """
    pattern = '|'.join(fields)
    return re.sub(f'({pattern})=[^{separator}]*', f'\\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION,message, self.SEPARATOR)
