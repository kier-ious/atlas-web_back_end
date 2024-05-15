#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""

import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
        """Format the specified lof records

        Args:
            record (logging.LogRecord): Logging record to format

        Returns:
            str: Formatted log msg w/ specified fields obfuscated
        """
        message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION, message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Returns a config'd logger object"""
    logger = logging.getLogger("user_data")

    logger.setLevel(logging.INFO)

    """Disabling sending to other loggers"""
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    """Adding StreamHandler to logger"""
    logger.addHandler(stream_handler)

    return logger
