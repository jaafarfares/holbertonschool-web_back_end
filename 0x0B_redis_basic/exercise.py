#!/usr/bin/env python3
"""
exercise file
"""
import redis
from functools import wraps
import uuid
from typing import Callable


def count_calls(func: Callable) -> Callable:
    """
    count_calls decorator that takes a single method
    Callable argument and returns a Callable. """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """ Incrementing values"""
        key = func.__qualname__
        self._redis.incr(key)
        return func(self, *args, **kwargs)
    return wrapper


class Cache:
    """_summary_
    """
    def __init__(self):
        """
        store an instance of the Redis client as a
        private variable named _redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
