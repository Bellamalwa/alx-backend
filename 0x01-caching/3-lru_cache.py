#!/usr/bin/python3
"""
This module is the LRU Cache System Module.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU (least recently used) Cache System Class inherited from BaseCaching
    HINT:
      Use of OrderedDict which keep order of insertion of keys
      The order shows how recently they were used.
      In the beginning is the least recently used and in the end,
      the most recently used.
      Any update OR query made to a key moves to the end (most recently used).
      If anything is added, it is added at the end (most recently used/added).
      All operations have O(1) time complexity.
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        First, add/ update the key by conventional methods.
        And also move the key to the end to show that it was recently used.
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """ Return an item from the cache given a key.
        If the key is not found, return None.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
