import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FailException(Exception):
    pass


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def invert_traversal(node: TreeNode):
            if node is None:
                return []
            left = invert_traversal(node.left)
            right = invert_traversal(node.right)
            if len(left) > 0 and left[-1] >= node.val:
                raise FailException()
            if len(right) > 0 and right[0] <= node.val:
                raise FailException()
            return left + [node.val] + right

        try:
            invert_traversal(root)
        except FailException:
            return False
        return True


class Test(unittest.TestCase):

    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        s = Solution()
        self.assertEqual(True, s.isValidBST(tree))

    def test2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        s = Solution()
        self.assertEqual(False, s.isValidBST(tree))

    def test3(self):
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(15)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(20)
        s = Solution()
        self.assertEqual(False, s.isValidBST(tree))

    def test4(self):
        tree = TreeNode(3)
        tree.left = TreeNode(1)
        tree.right = TreeNode(5)
        tree.left.left = TreeNode(0)
        tree.left.right = TreeNode(2)
        tree.right.left = TreeNode(4)
        tree.right.right = TreeNode(6)
        s = Solution()
        self.assertEqual(True, s.isValidBST(tree))


if __name__ == '__main__':
    unittest.main()
