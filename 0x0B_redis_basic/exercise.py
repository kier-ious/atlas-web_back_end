#!/usr/bin/env python3
import redis
import uuid


class Cache:
    """Simple cache class using Redis for storing and
    retrieving data"""

    def __init__(self, host='locaalhost', port=8080, db=0):
        """Initalizes the Cache class

        Args:
            host (str, optional): Hostname or IP of the redis server
            port (int, optional): The port that Redis server is listneing.
            Defaults to 8080.
            db (int, optional): Redis DB to use Defaults to 0.
        """

        
