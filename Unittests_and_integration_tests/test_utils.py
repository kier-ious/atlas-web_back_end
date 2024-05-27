#!/usr/bin/env python3
"""Testing utils"""
import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Test"""
    @parameterized.expand([
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b"),
    ])
    def test_access_nested_map(self):
