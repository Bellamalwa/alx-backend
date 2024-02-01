#!/usr/bin/python3
"""
This module contains the `BasicCache` class that inherits from the
`BaseCaching` Parent Class and is a caching system that stores data
in a dictionary.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class is a caching system that stores data in a dictionary.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache and updates the cache.
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
