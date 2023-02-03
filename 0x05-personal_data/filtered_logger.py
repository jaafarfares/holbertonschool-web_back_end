#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        pattern = rf"{field}=.*?{separator}"
        var = f"{field}={redaction}{separator}"
    return re.sub(pattern, var, message)
