import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []

        def backtrack(node: TreeNode, level: int):
            if node is None:
                return

            if level == len(res):
                res.append(node.val)
            else:
                res[level] = max(node.val, res[level])

            backtrack(node.left, level + 1)
            backtrack(node.right, level + 1)

        backtrack(root, 0)
        return res


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(9)
        s = Solution()
        self.assertEqual([1, 3, 9], s.largestValues(root))


if __name__ == '__main__':
    unittest.main()
