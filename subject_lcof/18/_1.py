import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        curr = prehead
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return prehead.next


class Test(unittest.TestCase):

    def test(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(4)
        expected.next.next.next = ListNode(5)

        s = Solution()
        actual = s.deleteNode(head, 3)

        while expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next


if __name__ == '__main__':
    unittest.main()
