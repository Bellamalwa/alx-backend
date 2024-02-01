#!/usr/bin/python3
"""
This module is the FIFO Cache System Module.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache System Class inherited from BaseCaching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # if the cache is full, remove the first item added
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)  # remove the first item added
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Get an item from the cache
        """
        if key and key in self.cache_data:
            # if the key is not empty and is in the cache, return the item
            return self.cache_data.get(key)
        else:
            return None
