#!/usr/bin/env python3
"""
first unittest
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest import mock, TestCase, main
from unittest.mock import patch


class TestAccessNestedMap(TestCase):
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
    get_json test class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        test get_json method
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = payload

        with mock.patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(url), payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    test momoize class
    """

    @unittest.expectedFailure
    def test_memoize(self):
        """
        test_memoize function
        """
        class TestClass:
            """test class"""

            @patch.object(TestMemoize.TestClass, 'a_method', return_value=42)
            @memoize
            def a_property(self):
                """method"""
                return self.a_method()

        test = TestClass()
        returned = test.a_property
        self.assertEqual(returned, 42)



if __name__ == '__main__':
    main()
