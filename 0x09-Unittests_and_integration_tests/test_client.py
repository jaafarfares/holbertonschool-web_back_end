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


    @patch('client.GithubOrgClient.public_repos')
    def test_public_repos(self, mock_public_repos):
        """
        method to test public_repos
        """
        mock_public_repos.return_value = [("repo1"), ("repo2"), ("repo3")]
        repos = GithubOrgClient("my-github-org").public_repos()
        self.assertEqual(repos, [("repo1"), ("repo2"), ("repo3")])
        mock_public_repos.assert_called_once()


if __name__ == '__main__':
    unittest.main()
