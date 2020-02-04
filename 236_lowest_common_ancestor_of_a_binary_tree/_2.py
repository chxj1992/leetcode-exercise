import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self) -> None:
        self.ancestor = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(n)
        Space: O(logn)
        """

        def find_target(node: TreeNode, p: TreeNode, q: TreeNode) -> int:
            count = 0
            if node is None:
                return count
            if node == p or node == q:
                count += 1
            count += find_target(node.left, p, q)
            count += find_target(node.right, p, q)
            if self.ancestor is None and count == 2:
                self.ancestor = node
            return count

        self.ancestor = None
        find_target(root, p, q)
        return self.ancestor


class Test(unittest.TestCase):

    def test1(self):
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        s = Solution()
        self.assertEqual(tree.right, s.lowestCommonAncestor(tree, tree.right.left, tree.right.right))
        self.assertEqual(tree, s.lowestCommonAncestor(tree, tree.left, tree.right.right))

    def test2(self):
        tree = TreeNode(3)
        tree.left = TreeNode(5)
        tree.right = TreeNode(1)
        tree.left.left = TreeNode(6)
        tree.left.right = TreeNode(2)
        tree.right.left = TreeNode(0)
        tree.right.right = TreeNode(8)
        tree.left.right.left = TreeNode(7)
        tree.left.right.right = TreeNode(4)

        s = Solution()
        self.assertEqual(tree.left, s.lowestCommonAncestor(tree, tree.left, tree.left.right.right))


if __name__ == '__main__':
    unittest.main()
