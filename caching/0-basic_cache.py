#!/usr/bin/python3
"""(Basic dictionary) Create a class BasicCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defining basic caching system with no limit"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds or updates item in cache
        Args:
            key: The key to look up and retrieve item from cache
            item: Actual item being stored in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item from cache based on key
        Args:
            key: The key to look up and retrieve item from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
