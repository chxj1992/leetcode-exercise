import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        curr = prehead
        while l1 or l2:
            if l1 is None:
                curr.next = l2
                break
            if l2 is None:
                curr.next = l1
                break

            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            else:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            curr = curr.next
        return prehead.next


class Test(unittest.TestCase):

    def test(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        expected.next.next.next.next.next = ListNode(4)

        s = Solution()
        actual = s.mergeTwoLists(l1, l2)

        while expected:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next


if __name__ == '__main__':
    unittest.main()
