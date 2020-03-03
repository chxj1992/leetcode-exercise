import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_num(l: ListNode) -> int:
            total = 0
            i = 0
            while l:
                total += l.val * (10 ** i)
                l = l.next
                i += 1

            return total

        def to_list(n: int) -> ListNode:
            prev = ListNode(-1)
            curr = prev
            while n > 0:
                curr.next = ListNode(n % 10)
                curr = curr.next
                n //= 10
            return ListNode(0) if prev.next is None else prev.next

        return to_list(to_num(l1) + to_num(l2))


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
