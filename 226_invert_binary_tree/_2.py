import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            tmp = node.left
            node.left = node.right
            node.right = tmp
            stack += [node.left, node.right]
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
        return self.assertTreeEqual(expected.left, actual.left) and self.assertTreeEqual(expected.right, actual.right)

    def test(self):
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)

        s = Solution()
        actual = s.invertTree(tree)

        expected = TreeNode(4)
        expected.left = TreeNode(7)
        expected.right = TreeNode(2)
        expected.left.left = TreeNode(9)
        expected.left.right = TreeNode(6)
        expected.right.left = TreeNode(3)
        expected.right.right = TreeNode(1)

        self.assertTreeEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
