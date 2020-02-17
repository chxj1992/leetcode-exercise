import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        路径总和 III
        https://leetcode-cn.com/interview/history/1/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6OTIzMTU%3D/path-sum-iii/
        """
        def recursion(node: TreeNode, s: int, started: bool):
            count = 0
            if node is None:
                return count
            if node.val == s:
                count = 1
            count += recursion(node.left, s - node.val, True) + recursion(node.right, s - node.val, True)
            if not started:
                count += recursion(node.left, s, False) + recursion(node.right, s, False)
            return count

        return recursion(root, sum, False)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)

        self.assertEqual(3, s.pathSum(root, 8))

    def test2(self):
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left.left = TreeNode(5)
        root.right.left.right = TreeNode(1)

        self.assertEqual(3, s.pathSum(root, 22))

    def test3(self):
        s = Solution()
        root = TreeNode(-2)
        root.right = TreeNode(-3)

        self.assertEqual(1, s.pathSum(root, -5))


if __name__ == '__main__':
    unittest.main()
