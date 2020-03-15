import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(a: TreeNode, b: TreeNode):
            if not b:
                return True
            if not a or a.val != b.val:
                return False
            return recur(a.left, b.left) and recur(a.right, b.right)

        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) if A and B else False


class Test(unittest.TestCase):

    def test1(self):
        a = TreeNode(3)
        a.left = TreeNode(4)
        a.right = TreeNode(5)
        a.left.left = TreeNode(1)
        a.left.right = TreeNode(2)

        b = TreeNode(4)
        b.left = TreeNode(1)

        s = Solution()
        self.assertEqual(True, s.isSubStructure(a, b))

    def test2(self):
        a = TreeNode(1)
        a.left = TreeNode(0)
        a.right = TreeNode(1)
        a.left.left = TreeNode(-4)
        a.left.right = TreeNode(-3)

        b = TreeNode(1)
        b.left = TreeNode(-4)

        s = Solution()
        self.assertEqual(False, s.isSubStructure(a, b))


if __name__ == '__main__':
    unittest.main()
