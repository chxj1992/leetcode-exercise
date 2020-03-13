import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            tmp = root.left
            root.left = self.mirrorTree(root.right)
            root.right = self.mirrorTree(tmp)
        return root


class Test(unittest.TestCase):

    def assertTreeEqual(self, expected: TreeNode, actual: TreeNode):
        if expected is None and actual is None:
            return True
        if expected is None:
            assert False, 'actual should be None'
        if actual is None:
            assert False, 'expected should not be None'
        if expected.val != actual.val:
            assert False, 'expected : %s , actual: %s' % (expected.val, actual.val)
        return self.assertTreeEqual(expected.left, actual.left) and self.assertTreeEqual(expected.right,
                                                                                         actual.right)

    def test(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        expected = TreeNode(4)
        expected.left = TreeNode(7)
        expected.right = TreeNode(2)
        expected.left.left = TreeNode(9)
        expected.left.right = TreeNode(6)
        expected.right.left = TreeNode(3)
        expected.right.right = TreeNode(1)

        s = Solution()
        actual = s.mirrorTree(root)
        self.assertTreeEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
