import unittest
from datetime import datetime

"""
实现一个LRU过期算法的KV cache, 所有KV过期间隔相同, 满足如下性质: 
1. 最多存储n对KV; 
2. 如果大于n个, 则随意剔除一个已经过期的KV; 
3. 如果没有过期的KV, 则按照LRU的规则剔除一个KV; 
4. 查询时如果已经过期, 则返回空;
"""


class Node:

    def __init__(self, key: str, val: str, expire_time: float):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.expire_time = expire_time

    def is_expired(self):
        return datetime.now().timestamp() > self.expire_time


class LRUCache:

    def __init__(self, n: int, expired_in_seconds: float):
        self.size = 0
        self.cap = n
        self.hash_map = {}
        self.linked_list = None
        self.head = None
        self.tail = None
        self.expire_queue = []
        self.expired_in_seconds = expired_in_seconds

    def get(self, key: str):
        if key not in self.hash_map:
            return None
        node = self.hash_map[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: str, value: str):
        if key not in self.hash_map:
            node = Node(key, value, datetime.now().timestamp() + self.expired_in_seconds)
            self.hash_map[key] = node
            self._insert_first(node)
            self.expire_queue.append(node)
        else:
            node = self.hash_map[key]
            node.val = value
            self._move_to_head(node)
        self._gc()

    def _insert_first(self, node: Node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def _move_to_head(self, node: Node):
        self._remove_node(node.key)
        self._insert_first(node)

    def _remove_node(self, key: str) -> bool:
        if key not in self.hash_map:
            return False
        node = self.hash_map[key]
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1
        return True

    def _gc(self):
        while self.size > self.cap:
            oldest_node: Node = self.expire_queue[0]
            if oldest_node.is_expired():
                self.expire_queue.pop(0)
                if not self._remove_node(oldest_node.key):
                    continue
                del self.hash_map[oldest_node.key]
            else:
                key = self.tail.key
                self._remove_node(key)
                del self.hash_map[key]


class Test(unittest.TestCase):

    def test1(self):
        r = LRUCache(2, 100000000)
        r.put('a', 'Andy')
        r.put('b', 'Bob')
        self.assertEqual('Andy', r.get('a'))
        r.put('c', 'Candy')
        self.assertIsNone(r.get('b'))


if __name__ == '__main__':
    unittest.main()
