import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        i = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            while root is None or root.left is None:
                i += 1
                root = stack.pop()
                if i == k:
                    return root.val
            root = root.left


class Test(unittest.TestCase):

    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        s = Solution()
        self.assertEqual(4, s.kthLargest(root, 1))

    def test2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        s = Solution()
        self.assertEqual(4, s.kthLargest(root, 3))


if __name__ == '__main__':
    unittest.main()
