import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        if head is None:
            return None
        next_node = head
        for i in range(k):
            if next_node.next is None and i < k - 1:
                return head
            next_node = next_node.next

        next_head = self.reverseKGroup(next_node, k)

        prev = next_head
        curr = head
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


class Test(unittest.TestCase):

    def test1(self):
        """
        给定这个链表：1->2->3->4->5
        当 k = 1 时，应当返回: 1->2->3->4->52
        """
        _1 = ListNode(1)
        _2 = ListNode(2)
        _3 = ListNode(3)
        _4 = ListNode(4)
        _5 = ListNode(5)
        _1.next = _2
        _2.next = _3
        _3.next = _4
        _4.next = _5

        s = Solution()

        node = s.reverseKGroup(_1, 1)
        self.assertIsNotNone(node)
        for i in [1, 2, 3, 4, 5]:
            self.assertEqual(i, node.val)
            node = node.next

    def test2(self):
        """
        给定这个链表：1->2->3->4->5
        当 k = 2 时，应当返回: 2->1->4->3->5
        """
        _1 = ListNode(1)
        _2 = ListNode(2)
        _3 = ListNode(3)
        _4 = ListNode(4)
        _5 = ListNode(5)
        _1.next = _2
        _2.next = _3
        _3.next = _4
        _4.next = _5

        s = Solution()

        node = s.reverseKGroup(_1, 2)
        self.assertIsNotNone(node)
        for i in [2, 1, 4, 3, 5]:
            self.assertEqual(i, node.val)
            node = node.next

    def test3(self):
        """
        给定这个链表：1->2->3->4->5
        当 k = 3 时，应当返回: 3->2->1->4->5
        """
        _1 = ListNode(1)
        _2 = ListNode(2)
        _3 = ListNode(3)
        _4 = ListNode(4)
        _5 = ListNode(5)
        _1.next = _2
        _2.next = _3
        _3.next = _4
        _4.next = _5

        s = Solution()

        node = s.reverseKGroup(_1, 3)
        self.assertIsNotNone(node)
        for i in [3, 2, 1, 4, 5]:
            self.assertEqual(i, node.val)
            node = node.next


if __name__ == '__main__':
    unittest.main()
