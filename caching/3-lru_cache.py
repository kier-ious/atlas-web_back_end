#!/usr/bin/python3
"""(LRU Caching)Create a class LRUCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines caching system with LRU"""
    def __init__(self):
        super().__init__()
        self.usage_history = []
        self.size = 0

    def put(self, key, item):
        """Adds or updates item in cache
        Args:
            key: The key to look up and retrieve item from cache
            item: Actual item being stored in the cache
        """
        if key is None or item is None:
            """If none exit method"""
            return

        if self.size >= self.MAX_ITEMS:
            """If the cache is full kick out least used item"""
            old_key = self.usage_history.pop(0)
            del self.cache_data[old_key]
            print("DISCARD:", old_key)
            self.size -= 1

        self.cache_data[key] = item

        if key in self.usage_history:
            self.usage_history.remove(key)
        self.usage_history.append(key)
        self.size += 1

    def get(self, key):
        """Retrieves item from cache"""
        if key in self.cache_data:
            self.usage_history.remove(key)
            self.usage_history.append(key)
            return self.cache_data[key]
        return None
