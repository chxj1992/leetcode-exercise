import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = [root]
        while queue:
            level = []
            while queue:
                node = queue.pop(0)
                if node is None:
                    continue
                level += [node.left, node.right]
            depth += 1
            queue += level
        return depth - 1


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        s = Solution()
        self.assertEqual(3, s.maxDepth(root))


if __name__ == '__main__':
    unittest.main()
