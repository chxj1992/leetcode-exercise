import unittest


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def isSubTree(h: ListNode, r: TreeNode):
            if h is None:
                return True
            if r is None:
                return False
            if h.val != r.val:
                return False
            return isSubTree(h.next, r.left) or isSubTree(h.next, r.right)

        if head is None:
            return True
        if root is None:
            return False
        return isSubTree(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


class Test(unittest.TestCase):

    def build_root1(self):
        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(1)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(6)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(1)
        root.right.left.right.right = TreeNode(3)
        return root

    def build_root2(self):
        root = TreeNode(1)
        root.right = TreeNode(1)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(1)
        root.right.left.left = TreeNode(9)
        return root

    def test1(self):
        s = Solution()

        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(6)

        self.assertEqual(True, s.isSubPath(head, self.build_root1()))

    def test2(self):
        s = Solution()

        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(6)
        head.next.next.next.next = ListNode(8)

        self.assertEqual(False, s.isSubPath(head, self.build_root1()))

    def test3(self):
        s = Solution()

        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(8)

        self.assertEqual(True, s.isSubPath(head, self.build_root1()))

    def test4(self):
        s = Solution()

        head = ListNode(1)
        head.next = ListNode(10)

        self.assertEqual(True, s.isSubPath(head, self.build_root2()))


if __name__ == '__main__':
    unittest.main()
