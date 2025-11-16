from collections import OrderedDict

# LRU cache - get the least recent or to put the most recent key to the end of the dict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move accessed key to end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop least recently used (first item)
            self.cache.popitem(last=False)

# Time - get: O(n) (because of remove on order list)

# Space - put: O(n) (same reason)