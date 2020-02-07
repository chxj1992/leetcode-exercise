import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            row = []
            node_row = []
            while queue:
                node = queue.pop(0)
                row.append(node.val)
                if node.left is not None:
                    node_row.append(node.left)
                if node.right is not None:
                    node_row.append(node.right)
            res.append(row)
            queue += node_row
        return res


class Test(unittest.TestCase):

    def test(self):
        tree = TreeNode(3)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)
        s = Solution()
        expected = [
            [3],
            [9, 20],
            [15, 7]
        ]
        self.assertEqual(expected, s.levelOrder(tree))


if __name__ == '__main__':
    unittest.main()
