#!/usr/bin/env python3
"""
exercise file
"""
import redis
import json
from functools import wraps
import uuid
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """count_calls
    decorator that takes a single method
    Callable argument and returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Incrementing values"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and
    outputs for a particular function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        input_list = f"{method.__qualname__}:inputs"
        output_list = f"{method.__qualname__}:outputs"
        input_str = str(args)
        self._redis.rpush(input_list, input_str)
        result = method(self, *args, **kwargs)
        output_str = str(result)
        self._redis.rpush(output_list, output_str)
        return result
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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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


def replay(self, func: Callable) -> str:
    """ Retrieves the input and output history of specified function stored
    in Redis and prints a summary of its past usage."""
    method = func.__qualname__
    inputs = f"{method}:inputs"
    outputs = f"{method}:outputs"
    input_list = self._redis.lrange(inputs, 0, -1)
    output_list = self._redis.lrange(outputs, 0, -1)
    number = self._redis.get(method).decode('utf-8')
    print(f"{method} was called {number} times:")
    for inp, out in zip(input_list, output_list):
        input_args = json.loads(inp)
        output_result = json.loads(out)
        print(f"{method}{tuple(input_args)} -> {output_result}")
