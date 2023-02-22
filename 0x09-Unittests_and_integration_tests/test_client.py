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
def test_public_repos(self, mock_get_json):
    """
    method to test public_repos
    """
    mock_payload = [{"name": "Microsoft"}, {"name": "Apple"}, {"name": "Amazon"}]
    mock_get_json.return_value = mock_payload
    client = GithubOrgClient("test-org")
    repos = client.public_repos()
    expected_repos = ["Microsoft", "Apple", "Amazon"]
    self.assertEqual(repos, expected_repos)
    mock_get_json.assert_called_once()
    client._public_repos_url.assert_called_once()



if __name__ == '__main__':
    unittest.main()
