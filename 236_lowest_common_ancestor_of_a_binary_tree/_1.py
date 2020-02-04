import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(n)
        Space: O(logN)
        Timeout!
        """
        def get_ancestor_list(node: TreeNode, target: TreeNode, ancestor_list: List[TreeNode]):
            current_node_ancestor_list = ancestor_list + [node]
            if node == target:
                return current_node_ancestor_list
            if node is None:
                return []
            left, right = [], []
            if node.left is not None:
                left = get_ancestor_list(node.left, target, current_node_ancestor_list)
            if node.right is not None:
                right = get_ancestor_list(node.right, target, current_node_ancestor_list)

            return left if left else right

        p_ancestor_list = get_ancestor_list(root, p, [])
        q_ancestor_list = get_ancestor_list(root, q, [])

        ancestor = None
        while p_ancestor_list and q_ancestor_list:
            p_ancestor = p_ancestor_list.pop(0)
            q_ancestor = q_ancestor_list.pop(0)
            if p_ancestor == q_ancestor:
                ancestor = p_ancestor
            else:
                break
        return ancestor


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
