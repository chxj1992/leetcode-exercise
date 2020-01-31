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
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


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
