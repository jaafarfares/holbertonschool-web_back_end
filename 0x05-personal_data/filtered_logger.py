#!/usr/bin/env python3
"""_summary_
"""
import re
from typing import List



def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    fields_pattern = '|'.join(fields)
    return re.sub(fields_pattern, redaction, message,  flags=re.S)
