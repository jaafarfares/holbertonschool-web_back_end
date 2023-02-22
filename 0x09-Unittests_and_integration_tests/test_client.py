#!/usr/bin/env python3
"""
first unittest
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest.mock import patch, PropertyMock
from unittest import mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client class
    """

    @parameterized.expand([("google"), ("abc")])
    @patch('client.get_json')
    def test_org(self, url, payload):
        """test org class"""
        self.assertEqual(GithubOrgClient(url).org, payload.return_value)
        payload.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """self descriptive"""
        mock_payload = [{"name": "Microsoft"}, {"name": "Apple"}]
        mocked_method.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = {"name_": "Microsoft"}
            response = GithubOrgClient('test-org')
            a = response._public_repos_url
            self.assertEqual(
                a, mocked_public.return_value
            )
            mocked_method.assert_called_once()
            mocked_public.assert_called_once()


if __name__ == '__main__':
    unittest.main()
