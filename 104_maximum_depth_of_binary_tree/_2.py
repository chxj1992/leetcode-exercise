import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if root is None:
            return 0
        stack = [root]
        while stack:
            max_depth += 1
            new_stack = []
            while stack:
                node = stack.pop()
                if node.left is not None:
                    new_stack.append(node.left)
                if node.right is not None:
                    new_stack.append(node.right)
            stack += new_stack

        return max_depth


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
