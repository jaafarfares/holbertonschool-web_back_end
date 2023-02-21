#!/usr/bin/env python3
"""
first unittest
"""
import unittest
from unittest.mock import patch, MagicMock
from utils import get_json, access_nested_map
from parameterized import parameterized
from collections.abc import Mapping


if __name__ == '__main__':
    unittest.main()


class TestAccessNestedMap(unittest.TestCase):
    """_summary_
    Args:
        unittest (TestCase): test_access_nested_map
    """
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
    ])
    def test_access_nested_map(self, i, a, b):
        """
        Parameterize a unit test
        """
        self.assertEqual(access_nested_map(i, a), b)

    @parameterized.expand([({}, ['a'], KeyError),
                          ({'a': 1}, ['a', 'b'], KeyError)])
    def test_access_nested_map_exception(self, i, a, ex):
        """_summary_
        Parameterize a unit test
        """
        self.assertRaises(ex)


class TestGetJson(unittest.TestCase):
    """
    get json test class
    """
    @patch('utils.requests')
    def test_get_json(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {{'test_url="http://example.com"',
                                            'test_payload={"payload": True}'},
                                           {'test_url="http://holberton.io"',
                                            'test_payload={"payload": False}'}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_json(), ('False', 'True'))
