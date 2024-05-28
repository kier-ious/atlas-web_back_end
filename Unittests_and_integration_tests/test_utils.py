#!/usr/bin/env python3
"""Testing utils"""
import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the correct value for valid paths.

        Args:
            nested_map (Mapping): The nested map to access
            path (Sequence): The path of keys to access in the nested map.
            expected (Any): The expected value at the end of the path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths.

        Args:
            nested_map (Mapping): The nested map to access
            path (Sequence): The path of keys to access in the nested map.
        """
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns the expected result from the mocked
        HTTP call.

        Parameters:
            test_url (str): The URL to send the GET request to.
            test_payload (dict): The expected JSON payload returned
            by the GET request.
        """
        with patch('request.get') as mock_get:
            """Create a mock response object w/ a json method
            that returns test_payload"""
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            """Call the get_json function and add result"""
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            """Assert that the GET method was called exactly once
            with the test_url"""
            mock_get.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()
