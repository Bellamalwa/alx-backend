#!/usr/bin/python3
"""
This module is the LFU Cache System Module.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used Caching Algorithm.
    Implements an auxiliar queue system that
    also takes count of the keys that are being
    used (put/get).
    """
    use_count = {}

    def __init__(self):
        """implements init from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """
        Method to put a new item into Cache key.
        If the key limit is reached, removes the
        Least Frequently Used key.
        That being the first key from the auxiliar
        queue structure.
        """
        if not key or not item:
            return
        if key not in self.cache_data.keys():
            # if cache is full, remove the least frequently used item
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                # Sort the use_count dictionary by value (use_count)
                lfu = dict(sorted(self.use_count.items(),
                           key=lambda item: item[1]))
                # Get the first key from the dictionary (least frequently used)
                del_key = list(lfu.keys())[0]
                print(f"DISCARD: {del_key}")
                # Delete the key from the cache data dictionary
                del self.cache_data[del_key]
                # Delete the key from the use_count dictionary
                del self.use_count[del_key]
            count = 0
        else:
            count = self.use_count[key] + 1
            del self.use_count[key]
        self.use_count[key] = count  # Increment use_count by 1
        # Add the new item to the cache_data dictionary
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the Cache by key.
        Everytime get() is called, the key used is
        sent to the last place of the queue system
        and its use count increments by 1.
        """
        if not key or key not in self.cache_data:
            return None
        count = self.use_count[key]
        del self.use_count[key]
        self.use_count[key] = count + 1
        return self.cache_data[key]
