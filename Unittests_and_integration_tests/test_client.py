#!/usr/bin/env python3
"""Testing client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class.
    The GithubOrgClient class is responsible for interacting with the Github
    API to retrieve info about organizations. This test suite verifies that the
    org method of the GithubOrgClient class returns the correct info for diff
    orgs.
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that checks if GithubOrgClient returns correct value
        Configure the mock to return a fixed response"""
        mock_get_json.return_value = {
            'name': org_name, 'description': 'Description of ' + org_name}
        """Create instance of the GithubOrgClient and call the org method"""
        client = GithubOrgClient(org_name)
        result = client.org
        """Verify that get_jsonwas called once w/ expected args"""
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/' + org_name)
        """Verify that the result matches the expected response"""
        self.assertEqual(result, {
            'name': org_name, 'description': 'Description of ' + org_name})

    def test_public_repos_url(self):
        """Test the _public_repos_url property of the GithubOrgClient class
        Define a know payload for the org method"""
        org_payload = {
            'repos_url': 'https://api.github.com/orgs/testorg/repos'}
        """Create and instance of GithubOrgClient"""
        client = GithubOrgClient('testorg')
        """Access the _public_repos_url property"""
        public_repos_url = client._public_repos_url
        """Verify that the property returns the expected URL"""
        expected_url = 'https://api.github.com/orgs/testorg/repos'
        self.assertEqual(public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()
