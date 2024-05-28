#!/usr/bin/env python3
"""Testing client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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

    @patch('client.GithubOrgClient.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos property of the GithubOrgClient class
        Mock get_json and _public_repos_url
        Test that the list of repos is what you expect from the chosen payload
        Test that the mocked property and the mocked get_json was called once.
        Define  known payload for the get_json method
        """
        repos_payload = [
            {'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}
            ]
        """Define a known URL for the _public_repos_url property"""
        public_repos_url = 'https://api.github.com/orgs/testorg/repos'
        """Patch the _public_repos_url property to return the known url"""
        mock_public_repos_url.return_value = public_repos_url
        """Patch the get_json method to return the known payload"""
        mock_get_json.return_value = repos_payload
        """Create an instance of the GithubOrgClient"""
        client = GithubOrgClient('testorg')
        """Access the public_repos property"""
        public_repos = client.public_repos
        """Verify that the property returns the expected list of repos"""
        expected_repos = [
            {'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}]
        self.assertEqual(public_repos, expected_repos)
        """Verify that the mocked property & get_json were called only once"""
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(public_repos_url)


if __name__ == '__main__':
    unittest.main()
