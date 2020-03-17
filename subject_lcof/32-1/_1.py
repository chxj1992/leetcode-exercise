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
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue += [node.left, node.right]
        return res


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        s = Solution()
        self.assertEqual([3, 9, 20, 15, 7], s.levelOrder(root))


if __name__ == '__main__':
    unittest.main()
