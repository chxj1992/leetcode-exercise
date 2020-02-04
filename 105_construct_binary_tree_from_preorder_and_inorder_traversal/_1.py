import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:left_index + 1], inorder[0:left_index])
        root.right = self.buildTree(preorder[left_index + 1:], inorder[left_index + 1:])
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
        """
        前序遍历 preorder = [3,9,20,15,7]
        中序遍历 inorder = [9,3,15,20,7]
        """
        tree = TreeNode(3)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)
        s = Solution()
        self.assertTreeEqual(tree, s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))


if __name__ == '__main__':
    unittest.main()
