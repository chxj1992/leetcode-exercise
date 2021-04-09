import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev, incr = ListNode(), 0
        curr = prev
        while l1 is not None or l2 is not None:
            val = incr
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            incr = 1 if val > 9 else 0
            curr.next = ListNode(val % 10)
            curr = curr.next
        if incr == 1:
            curr.next = ListNode(1)
        return prev.next


class Test(unittest.TestCase):

    def test1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        expected = ListNode(7)
        expected.next = ListNode(0)
        expected.next.next = ListNode(8)
        s = Solution()
        actual = s.addTwoNumbers(l1, l2)

        while expected:
            self.assertEqual(expected.val, actual.val)
            actual = actual.next
            expected = expected.next

    def test2(self):
        l1 = ListNode(1)
        l1.next = ListNode(8)
        l2 = ListNode(0)
        expected = ListNode(1)
        expected.next = ListNode(8)
        s = Solution()
        actual = s.addTwoNumbers(l1, l2)

        while expected:
            self.assertEqual(expected.val, actual.val)
            actual = actual.next
            expected = expected.next


if __name__ == '__main__':
    unittest.main()
