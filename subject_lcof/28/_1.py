import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(sub1: TreeNode, sub2: TreeNode):
            if not sub1 and not sub2:
                return True
            elif not sub1 or not sub2:
                return False
            return sub1.val == sub2.val and symmetric(sub1.left, sub2.right) and symmetric(sub1.right, sub2.left)
        if root is None:
            return True
        return symmetric(root.left, root.right)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        s = Solution()
        self.assertEqual(True, s.isSymmetric(root))


if __name__ == '__main__':
    unittest.main()
