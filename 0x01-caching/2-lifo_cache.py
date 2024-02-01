#!/usr/bin/python3
"""
This module is the LIFO Cache System Module.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache System Class inherited from BaseCaching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item  # Add item in the cache
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # if the cache is full, remove the last item added
            self.cache_data.pop(self.last_item)  # remove the last item added
            print("DISCARD:", self.last_item)  # print the last item discarded
        if key:
            # if the key is not empty, set the last_put to the key added
            self.last_item = key

    def get(self, key):
        """ Get an item from the cache
        """
        return self.cache_data.get(key)
