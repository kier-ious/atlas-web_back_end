#!/usr/bin/env python3
"""Testing utils"""
import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map


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

    @parameterized.expand({
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    })
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths.

        Args:
            nested_map (Mapping): The nested map to access
            path (Sequence): The path of keys to access in the nested map.
        """
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
