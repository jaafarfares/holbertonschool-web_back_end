#!/usr/bin/env python3
"""
first unittest
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest.mock import patch
from unittest import mock


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client class
    """

    @parameterized.expand([(google), (abc)])
    def test_org(self, ):
        """test org class"""
        
