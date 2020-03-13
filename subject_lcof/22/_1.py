import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        prev = head
        i = 1
        while head:
            if i > k:
                prev = prev.next
            head = head.next
            i += 1
        return prev


class Test(unittest.TestCase):

    def test(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        expected = ListNode(4)
        expected.next = ListNode(5)

        s = Solution()
        actual = s.getKthFromEnd(head, 2)

        while expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next


if __name__ == '__main__':
    unittest.main()
