#!/usr/bin/env python3
"""_summary_
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """_summary_

    Args:
        fields (List[str]): _description_
        redaction (str): _description_
        message (str): _description_
        separator (str): _description_

    Returns:
        str: _description_
    """
    for field in fields:
        pattern = rf"{field}=[^;]+"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
