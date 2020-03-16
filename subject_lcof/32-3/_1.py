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
        level = 1
        queue = [root]
        res = [[root.val]]
        while queue:
            level += 1
            row = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)
            queue = row
            if row:
                l = row if level % 2 == 1 else row[::-1]
                res.append([x.val for x in l])
        return res


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        s = Solution()
        self.assertEqual([
            [3],
            [20, 9],
            [15, 7]
        ], s.levelOrder(root))


if __name__ == '__main__':
    unittest.main()
