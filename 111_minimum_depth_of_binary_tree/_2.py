import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        min_depth = 0
        stack = [root]
        while stack:
            min_depth += 1
            new_stack = []
            while stack:
                node = stack.pop()
                if node is None:
                    continue
                new_stack += [node.left, node.right]
                if node.left is None and node.right is None:
                    return min_depth
            stack = new_stack
        return min_depth


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
