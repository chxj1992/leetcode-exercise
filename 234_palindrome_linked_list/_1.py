import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        node = ListNode(1)
        node.next = ListNode(2)
        self.assertEqual(False, s.isPalindrome(node))

    def test2(self):
        s = Solution()
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(2)
        node.next.next.next = ListNode(1)
        self.assertEqual(True, s.isPalindrome(node))


if __name__ == '__main__':
    unittest.main()
