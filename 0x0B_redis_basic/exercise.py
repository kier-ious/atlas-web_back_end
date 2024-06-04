#!/usr/bin/env python3
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Decorator to cound how many times a method is called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment count in Redis & call method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Simple cache class using Redis for storing and
    retrieving data"""

    def __init__(self, host='localhost', port=6379, db=0):
        """Initializes the Cache class

        Args
            host (str, optional): Hostname or IP of the redis server
            port (int, optional): The port that Redis server is listening.
            Defaults to 6379.
            db (int, optional): Redis DB to use Defaults to 0.
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in the cache and returns generated key

        Args:
            data (Union[str, bytes, int, float]): the data to be cached
        Returns:
            str: The random key used to store the data
        """
        key = str(uuid.uuid4()) # Random key
        self._redis.set(key, data) # Storing data in Redis
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Retrieves data from the cache and converts it to desired format"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str):
        """Retrieves data from cache and converts to a string"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str):
        """Retrieves data from cache and converts to an integer"""
        return self.get(key, fn=lambda d: int(d.decode('utf-8')))

    def incr(self, key: str) -> str:
        """Increments the int value of a key by 1 and returns new value"""
        return self._redis.incr(key)
