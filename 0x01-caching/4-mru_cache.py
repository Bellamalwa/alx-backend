#!/usr/bin/python3
"""
This module is the MRU Cache System Module.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU (most recently used) Cache System Class inherited from BaseCaching
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        First, add/ update the key by conventional methods.
        And also move the key to the end to show that it was recently used.
        So, if number of items in the cache is greater than the MAX_ITEMS,
        discard the most recently used item (MRU algorithm).
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # if cache is full, remove the most recently used item
                if key in self.cache_data:
                    # Update the key by conventional methods
                    self.cache_data.update({key: item})
                    # Set the most recently used key to the key added
                    self.mru = key
                else:
                    # Set the key to be discarded to the most recently used key
                    discard_key = self.mru
                    # Delete the key from the cache data dictionary
                    del self.cache_data[discard_key]
                    print("DISCARD: {}".format(discard_key))
                    self.cache_data.update({key: item})
                    self.mru = key
            else:
                self.cache_data.update({key: item})
                self.mru = key

    def get(self, key):
        """ Return an item from the cache
        First, check if the key is in the cache.
        If so, move the key to the end of the dictionary.
        """
        if key in self.cache_data:
            self.mru = key  # Set the most recently used key to the key added
            return self.cache_data[key]
        return None
