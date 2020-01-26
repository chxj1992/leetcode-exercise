import unittest
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class Test(unittest.TestCase):

    def test(self):
        """
        ["LRUCache", "put", "put", "put", "put", "get", "get"]
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
        """
        r = LRUCache(2)
        self.assertIsNone(r.put(2, 1))
        self.assertIsNone(r.put(1, 1))
        self.assertIsNone(r.put(2, 3))
        self.assertIsNone(r.put(4, 1))
        self.assertEqual(r.get(1), -1)
        self.assertEqual(r.get(2), 3)


if __name__ == '__main__':
    unittest.main()
