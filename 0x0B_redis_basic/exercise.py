#!/usr/bin/env python3
import redis
import uuid
from typing import Union


class Cache:
    """Simple cache class using Redis for storing and
    retrieving data"""

    def __init__(self, host='locaalhost', port=6379, db=0):
        """Initializes the Cache class

        Args:
            host (str, optional): Hostname or IP of the redis server
            port (int, optional): The port that Redis server is listening.
            Defaults to 8080.
            db (int, optional): Redis DB to use Defaults to 0.
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        # self.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in the cache and returns generated key

        Args:
            data (Union[str, bytes, int, float]): the data to be cached
        Returns:
            str: The random key used to store the data
        """
        key = str(uuid.uuid4()) # Random key
        self.redis.set(key, data) # Storing data in Redis
        return key

    def flushdb(self) -> None:
        """Flushes the cache"""
        self._redis.flushdb()
