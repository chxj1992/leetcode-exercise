import unittest

# Definition for singly-linked list.
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0]
        i = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:len(inorder[:i]) + 1], inorder[:i])
        root.right = self.buildTree(preorder[len(inorder[:i]) + 1:], inorder[i + 1:])
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
        s = Solution()

        expected = TreeNode(3)
        expected.left = TreeNode(9)
        expected.right = TreeNode(20)
        expected.right.left = TreeNode(15)
        expected.right.right = TreeNode(7)

        actual = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

        self.assertTreeEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
