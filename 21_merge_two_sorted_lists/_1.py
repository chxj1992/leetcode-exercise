import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)
        curr = prehead
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 is not None else l2

        return prehead.next


class Test(unittest.TestCase):

    def test1(self):
        """
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        a_1 = ListNode(1)
        a_2 = ListNode(2)
        a_4 = ListNode(4)
        a_1.next = a_2
        a_2.next = a_4

        b_1 = ListNode(1)
        b_3 = ListNode(3)
        b_4 = ListNode(4)
        b_1.next = b_3
        b_3.next = b_4

        s = Solution()
        node = s.mergeTwoLists(a_1, b_1)

        self.assertIsNotNone(node)
        for i in [1, 1, 2, 3, 4, 4]:
            self.assertEqual(i, node.val)
            node = node.next


if __name__ == '__main__':
    unittest.main()
