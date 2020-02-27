import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        """
        N叉树的前序遍历
        https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
        """
        stack = []
        res = []
        while root is not None or stack:
            while root is not None:
                res.append(root.val)
                stack.append(root)
                root = root.children.pop(0) if root.children else None
            root = stack.pop()
            while stack and not root.children:
                root = stack.pop()
            if root.children is not None and len(root.children) > 1:
                stack.append(root)
            root = root.children.pop(0) if root.children else None
        return res


class Test(unittest.TestCase):

    def test(self):
        root = Node(1, [])
        root.children += [Node(3, []), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]

        s = Solution()
        self.assertEqual([1, 3, 5, 6, 2, 4], s.preorder(root))


if __name__ == '__main__':
    unittest.main()
