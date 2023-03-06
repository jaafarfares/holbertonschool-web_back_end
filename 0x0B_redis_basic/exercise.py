#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from collections.abc import Callable


def count_calls(method: Callable)-> Callable:
    return

class Cache:
    """_summary_
    """
    def __init__(self):
        """
        store an instance of the Redis client as a
        private variable named _redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """generate a random key (e.g. using uuid),
        store the input data in
        Redis using the random key and return the key."""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> str:
        """take a key string argument and an optional Callable argument
        named fn. This callable will beused to convert the data back to
        the desired format."""
        if (self._redis.exists(key)):
            value = self._redis.get(key)
            if fn is None:
                return value

            return fn(value)
        return None

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get
        with the correct conversion function
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get
        with the correct conversion function
        """
        return self.get(key, int)
