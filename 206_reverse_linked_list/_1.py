import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


class Test(unittest.TestCase):

    def test(self):
        """
        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
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
        node = s.reverseList(_1)

        self.assertIsNotNone(node)
        i = 5
        while node is not None:
            self.assertEqual(i, node.val)
            node = node.next
            i -= 1


if __name__ == '__main__':
    unittest.main()
