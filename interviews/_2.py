import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def max_depth(node: TreeNode) -> int:
            depth = 0
            stack = [node]
            while stack:
                row = []
                while stack:
                    node = stack.pop()
                    if node is None:
                        continue
                    row += [node.left, node.right]
                if row:
                    depth += 1
                    stack = row
            return depth

        while root is not None:
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)
            diameter = max(diameter, left_depth + right_depth)
            root = root.left if left_depth > right_depth else root.right

        return diameter


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(3, s.diameterOfBinaryTree(root))


if __name__ == '__main__':
    unittest.main()
