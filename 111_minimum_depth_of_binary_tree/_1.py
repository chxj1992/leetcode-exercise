import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def min_depth(node: TreeNode, level: int) -> int:
            if node is None:
                return level
            left = min_depth(node.left, level + 1)
            right = min_depth(node.right, level + 1)
            if node.left is None:
                return right
            if node.right is None:
                return left
            return min(left, right)

        return min_depth(root, 0)


class Test(unittest.TestCase):

    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        s = Solution()
        self.assertEqual(2, s.minDepth(tree))

    def test2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        s = Solution()
        self.assertEqual(2, s.minDepth(tree))

    def test3(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        s = Solution()
        self.assertEqual(2, s.minDepth(tree))


if __name__ == '__main__':
    unittest.main()
