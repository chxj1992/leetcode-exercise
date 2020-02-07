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
        queue = [root]
        while queue:
            x = None
            row = []
            while queue:
                node = queue.pop()
                if node is None:
                    continue
                if x is None or x < node.val:
                    x = node.val
                row += [node.left, node.right]
            if x is not None:
                res.append(x)
            queue = row

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
