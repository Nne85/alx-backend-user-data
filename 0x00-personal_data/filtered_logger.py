#!/usr/bin/env python3
"""
Returns Log Message
"""

import re
import logging
from typing import List

PII_FIELDS = ("name", "email", "phone_number", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message using a redaction string.

    Args:
        fields (List[str]):A list of strings representing fields to obfuscate.
        redaction (str): A string representing the value by which the fields
        will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing the character separating all
        fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    pattern = rf"(?<={separator})({'|'.join(fields)})=(.*?)(?={separator})"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


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
        """Obfuscates specified fields in the log message and
        formats the record."""
        msg = super(RedactingFormatter, self).format(record)
        text = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return text

def get_logger() -> logging.Logger:
    """  returns a logging.Logger object. """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    main()
