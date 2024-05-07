#!/usr/bin/python3
"""(FIFO caching)Create a class FIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines caching system with FIFO"""
    def __init__(self):
        super().__init__()
        self.queue = []
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
            """If cache full kick first item out"""
            trash_key = self.queue.pop(0)
            del self.cache_data[trash_key]
            print("DISCARD:", trash_key)
            self.size -= 1

        self.cache_data[key] = item
        self.queue.append(key)
        self.size += 1

    def get(self, key):
        """Retrieves item from cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
