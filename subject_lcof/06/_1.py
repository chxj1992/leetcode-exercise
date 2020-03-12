import unittest

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]


class Test(unittest.TestCase):

    def test(self):
        head = ListNode(1)
        head.next = ListNode(3)
        head.next.next = ListNode(2)
        s = Solution()
        self.assertEqual([2, 3, 1], s.reversePrint(head))


if __name__ == '__main__':
    unittest.main()
