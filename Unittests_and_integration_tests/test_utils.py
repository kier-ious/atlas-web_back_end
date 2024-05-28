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
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand({
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    })
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)
            """Verify the exception msg"""
            self.assertEqual(str(ke.exception), str(path[-1]))


if __name__ == '__main__':
    unittest.main()
