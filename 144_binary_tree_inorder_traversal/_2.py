import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = []
        res = []
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                res.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


class Test(unittest.TestCase):

    def test(self):
        tree = TreeNode(1)
        right = TreeNode(2)
        right.left = TreeNode(3)
        tree.right = right
        s = Solution()
        self.assertEqual([1, 2, 3], s.preorderTraversal(tree))


if __name__ == '__main__':
    unittest.main()
