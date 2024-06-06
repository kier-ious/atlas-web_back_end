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


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs
    for a particular function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper funciton to store input/output history in Redis"""
        """Prepare the Redis keys for the inputs/outputs"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        """Log the inout args"""
        self._redis.rpush(input_key, str(args))
        """Call the original method and get the output"""
        output = method(self, *args, **kwargs)
        """log the output"""
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable):
    """Display the history of the calls of a particular funciton"""
    """Prepare the redis keys for inputs/outputs"""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    """Retrieve the inputs/outputs from redis"""
    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    """Print the call history"""
    print(f"{method.__qualname__} was called{len(inputs)} times:")
    for input_, output in zip(inputs, outputs):
        """Decode input/output from bytes to str and print the details"""
        input_str = input_.decode('utf-8')
        output_str = output.decode('utf-8')
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


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
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in the cache and returns generated key

        Args:
            data (Union[str, bytes, int, float]): the data to be cached
        Returns:
            str: The random key used to store the data
        """
        key = str(uuid.uuid4())
        """Random key"""
        self._redis.set(key, data)
        """Storing data in Redis"""
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
