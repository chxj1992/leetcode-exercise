import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        class NotBalanced(Exception):
            pass

        def max_depth(node: TreeNode):
            if node is None:
                return 0

            left = max_depth(node.left)
            right = max_depth(node.right)
            if abs(left - right) >= 2:
                raise NotBalanced()
            return max(left, right) + 1

        try:
            max_depth(root)
        except NotBalanced:
            return False
        return True


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        s = Solution()
        self.assertEqual(True, s.isBalanced(root))


if __name__ == '__main__':
    unittest.main()
