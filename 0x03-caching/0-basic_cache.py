#!/usr/bin/python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
import requests
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
