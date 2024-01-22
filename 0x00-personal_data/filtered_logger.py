#!/usr/bin/env python3
"""
Returns Log Message
"""

import re
from typing import List


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


if __name__ == "__main__":
    main()
