import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def recursion(node: TreeNode, level: int):
            if node is None:
                return
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            recursion(node.left, level + 1)
            recursion(node.right, level + 1)

        recursion(root, 0)
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
