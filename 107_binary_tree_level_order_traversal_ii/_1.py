import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            next_level = []
            row = []
            while queue:
                node = queue.pop(0)
                if node is None:
                    continue
                row.append(node.val)
                next_level += [node.left, node.right]
            if row:
                res.insert(0, row)
            queue = next_level
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [
            [15, 7],
            [9, 20],
            [3]
        ]

        self.assertEqual(expected, s.levelOrderBottom(root))


if __name__ == '__main__':
    unittest.main()
