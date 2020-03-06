import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pass


class Test(unittest.TestCase):

    def test1(self):
        """
        head = [3,2,0,-4], pos = 1
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）
        如果 pos 是 -1，则在该链表中没有环
        """
        _1 = ListNode(3)
        _2 = ListNode(2)
        _3 = ListNode(0)
        _4 = ListNode(-4)
        _1.next = _2
        _2.next = _3
        _3.next = _4
        _4.next = _2

        s = Solution()
        node = s.detectCycle(_1)
        self.assertEqual(_2, node)

    def test2(self):
        """
        [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
        -1
        """
        l = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21,
             5]
        n = len(l)
        head = ListNode(l[0])
        node = head
        for i in range(n - 1):
            node.next = ListNode(l[i + 1])
            node = node.next
        s = Solution()
        self.assertIsNone(s.detectCycle(head))


if __name__ == '__main__':
    unittest.main()
