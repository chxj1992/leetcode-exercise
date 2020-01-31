import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            res.append(node.val)
            stack += [node.left, node.right]
        return res[::-1]


class Test(unittest.TestCase):

    def test1(self):
        tree = TreeNode(1)
        right = TreeNode(2)
        right.left = TreeNode(3)
        tree.right = right
        s = Solution()
        self.assertEqual([3, 2, 1], s.postorderTraversal(tree))

    def test2(self):
        tree = TreeNode(3)
        tree.left = TreeNode(1)
        tree.right = TreeNode(2)
        s = Solution()
        self.assertEqual([1, 2, 3], s.postorderTraversal(tree))


if __name__ == '__main__':
    unittest.main()
