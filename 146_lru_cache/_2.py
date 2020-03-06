import unittest


class LinkNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.cap = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        node = self.items[key]
        if self.head is not node:
            self._remove_node(key)
            self._add_first(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            node = self.items[key]
            node.val = value
            if self.head is not node:
                self._remove_node(key)
                self._add_first(node)
        else:
            node = LinkNode(key, value)
            self._add_first(node)
            self._clear()

    def _add_first(self, node: LinkNode):
        self.size += 1
        self.items[node.key] = node
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def _remove_node(self, key):
        node = self.items[key]
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        elif node.prev is not None:
            self.tail = node.prev

        self.size -= 1
        del self.items[key]

    def _clear(self):
        while self.size > self.cap:
            curr_tail = self.tail
            self.tail = self.tail.prev
            self._remove_node(curr_tail.key)


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
