import unittest


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


class Test(unittest.TestCase):

    def test1(self):
        """
        ["LRUCache", "put", "put", "put", "put", "get", "get"]
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
        """
        r = LRUCache(2)
        r.put(2, 1)
        r.put(1, 1)
        r.put(2, 3)
        r.put(4, 1)
        self.assertEqual(-1, r.get(1))
        self.assertEqual(3, r.get(2))

    def test2(self):
        """
        ["LRUCache", "put", "put", "put", "put", "get", "get"]
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
        """
        r = LRUCache(2)
        r.put(1, 1)
        r.put(2, 2)
        self.assertEqual(1, r.get(1))
        r.put(3, 3)
        self.assertEqual(-1, r.get(2))
        r.put(4, 4)
        self.assertEqual(-1, r.get(1))
        self.assertEqual(3, r.get(3))
        self.assertEqual(4, r.get(4))

    def test3(self):
        """
        ["LRUCache","put","get","put","get","get"]
        [[1],[2,1],[2],[3,2],[2],[3]]
        """
        r = LRUCache(1)
        r.put(2, 1)
        self.assertEqual(1, r.get(2))
        r.put(3, 2)
        self.assertEqual(-1, r.get(2))
        self.assertEqual(2, r.get(3))

    def test4(self):
        """
        ["LRUCache","put","put","get","get","put","get","get","get"]
        [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
        """
        r = LRUCache(2)
        r.put(2, 1)
        r.put(3, 2)
        self.assertEqual(2, r.get(3))
        self.assertEqual(1, r.get(2))
        r.put(4, 3)
        self.assertEqual(1, r.get(2))
        self.assertEqual(-1, r.get(3))
        self.assertEqual(3, r.get(4))


if __name__ == '__main__':
    unittest.main()
