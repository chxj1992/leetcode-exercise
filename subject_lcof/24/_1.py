import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


class Test(unittest.TestCase):

    def test(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        expected = ListNode(5)
        expected.next = ListNode(4)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(1)

        s = Solution()
        actual = s.reverseList(head)

        while expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next


if __name__ == '__main__':
    unittest.main()
