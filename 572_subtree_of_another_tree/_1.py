import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val == t.val:
            if self.tree_equals(s.left, t.left) and self.tree_equals(s.right, t.right):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def tree_equals(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.tree_equals(t1.left, t2.left) and self.tree_equals(t1.right, t2.right)


class Test(unittest.TestCase):

    def test1(self):
        solution = Solution()

        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        self.assertTrue(solution.isSubtree(s, t))

    def test2(self):
        solution = Solution()

        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)
        s.left.right.left = TreeNode(0)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        self.assertFalse(solution.isSubtree(s, t))


if __name__ == '__main__':
    unittest.main()
