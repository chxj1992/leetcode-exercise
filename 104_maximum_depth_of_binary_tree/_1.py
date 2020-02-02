import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def max_depth(node: TreeNode, level: int) -> int:
            if node is None:
                return level
            return max(max_depth(node.left, level + 1), max_depth(node.right, level + 1))

        return max_depth(root, 0)


class Test(unittest.TestCase):

    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        s = Solution()
        self.assertEqual(2, s.maxDepth(tree))

    def test2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        s = Solution()
        self.assertEqual(3, s.maxDepth(tree))


if __name__ == '__main__':
    unittest.main()
