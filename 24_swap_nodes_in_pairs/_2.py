import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        if head is None or head.next is None:
            return head
        node = self.swapPairs(head.next.next)
        new_head = head.next
        new_head.next = head
        head.next = node
        return new_head


class Test(unittest.TestCase):

    def test(self):
        """
        给定 1->2->3->4,
        你应该返回 2->1->4->3.
        """
        _1 = ListNode(1)
        _2 = ListNode(2)
        _3 = ListNode(3)
        _4 = ListNode(4)
        _1.next = _2
        _2.next = _3
        _3.next = _4

        s = Solution()
        node = s.swapPairs(_1)

        self.assertIsNotNone(node)
        for i in [2, 1, 4, 3]:
            self.assertEqual(i, node.val)
            node = node.next


if __name__ == '__main__':
    unittest.main()
