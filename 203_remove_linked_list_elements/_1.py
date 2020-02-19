import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        curr = prev
        while curr is not None:
            if curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return prev.next


class Test(unittest.TestCase):

    def test1(self):
        node = ListNode(1)
        _2 = ListNode(2)
        _3 = ListNode(6)
        _4 = ListNode(3)
        _5 = ListNode(4)
        _6 = ListNode(5)
        _7 = ListNode(6)
        node.next = _2
        _2.next = _3
        _3.next = _4
        _4.next = _5
        _5.next = _6
        _6.next = _7

        s = Solution()
        node = s.removeElements(node, 6)

        self.assertIsNotNone(node)
        while node is not None:
            self.assertNotEqual(6, node.val)
            node = node.next

    def test2(self):
        node = ListNode(1)

        s = Solution()
        node = s.removeElements(node, 1)

        self.assertIsNone(node)

    def test3(self):
        node = ListNode(1)
        _2 = ListNode(1)
        node.next = _2

        s = Solution()
        node = s.removeElements(node, 1)

        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()
