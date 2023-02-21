#!/usr/bin/env python3
"""
first unittest
"""
import unittest
from unittest.mock import patch, MagicMock, Mock
from utils import *
from parameterized import parameterized
from collections.abc import Mapping


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
    @parameterized.expand([('test_url=http://example.com',
                            {"payload": True}),
                           ('test_url=http://holberton.io',
                            {"payload": False})])
    def test_get_json(self, url, payload):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(url), payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    test momoize class
    """

    def test_memoize():
        """
        test_memoize function
        """
        class TestClass:
            """test class"""

            def a_method(self):
                """method"""
                return 42

            @memoize
            @patch.object(TestMemoize.TestClass, 'a_method', return_value=42)
            def a_property(self):
                """method"""
            test = TestMemoize.TestClass()
            returne = test.a_property
            self.assertEqual(returne, 42)
                return self.a_method()


if __name__ == '__main__':
    unittest.main()
