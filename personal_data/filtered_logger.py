#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""

import re
from typing import List
import logging
import os
import mysql.connector


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to secure DB and returns a MySQLConnection object"""
    """Get DB credentials from env vars"""
    PERSONAL_DATA_DB_USERNAME = os.environ.get(
        "PERSONAL_DATA_DB_USERNAME", "root")
    PERSONAL_DATA_DB_PASSWORD = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    PERSONAL_DATA_DB_HOST = os.environ.get(
        "PERSONAL_DATA_DB_HOST", "localhost")
    PERSONAL_DATA_DB_NAME = os.environ.get("PERSONAL_DATA_DB_NAME", "")

    """Connection to mySQL DB"""
    db = mysql.connector.connect(
        user=PERSONAL_DATA_DB_USERNAME,
        password=PERSONAL_DATA_DB_PASSWORD,
        host=PERSONAL_DATA_DB_HOST,
        database=PERSONAL_DATA_DB_NAME
    )

    return db


def main():
    """The function will obtain a database connection using
    get_db and retrieve all rows in the users table and display
    each row under a filtered format like this"""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor.fetchall():
        """Made filtered dictionary when sensitive info is replaced
        by ***"""
        filtered_row = {
            field: "***" if field in PII_FIELDS else value
            for field, value in zip(cursor.description, row)
        }
        """Convert about dict into formatted str"""
        formatted_row = "; ".join(
            [f"{key}={value}" for key, value in filtered_row.items()])
        """Log the new formatted row with logger object"""
        logger.info(formatted_row)
    cursor.close()
    db.close()
