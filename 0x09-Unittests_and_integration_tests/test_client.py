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


@parameterized.expand([
        ("org", "repos", ["repo1", "repo2", "repo3"], ["repo2"]),
        ("org", "repos_no_license", ["repo1", "repo3"], ["repo1", "repo3"])
    ])
def test_public_repos(self, org_payload, expected_repos, apache2_repos):
    """
    Test GithubOrgClient.public_repos
    """
    with patch('client.public_repos') as mock_get_json:
        mock_get_json.side_effect = [
            {"repos_url": f"https://api.github.com/{org_payload}/repos"},
            [{"name": repo, "license": {"key": "apache-2.0"}} if repo in apache2_repos else {"name": repo, "license": None} for repo in expected_repos]
        ]
        client = GithubOrgClient("my-github-org")
        repos = client.public_repos()
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called()
        client._public_repos_url.assert_called()
        repos = client.public_repos("apache-2.0")
        self.assertEqual(repos, apache2_repos)


if __name__ == '__main__':
    unittest.main()
