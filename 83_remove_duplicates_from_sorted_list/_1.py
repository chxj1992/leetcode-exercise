import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        l = ListNode(1)
        l.next = ListNode(1)
        l.next.next = ListNode(2)

        actual = s.deleteDuplicates(l)

        expected = ListNode(1)
        expected.next = ListNode(2)

        while expected is not None:
            self.assertEqual(actual.val, expected.val)
            actual = actual.next
            expected = expected.next


if __name__ == '__main__':
    unittest.main()
