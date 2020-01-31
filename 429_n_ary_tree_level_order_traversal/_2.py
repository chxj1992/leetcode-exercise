import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: Node) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []
        self.levelOrderTraversal(root, 0)
        return self.res

    def levelOrderTraversal(self, root: Node, i: int):
        if i == len(self.res):
            self.res.append([])
        if root is not None:
            self.res[i] += [root.val]
            if root.children is not None:
                for child in root.children:
                    self.levelOrderTraversal(child, i + 1)


class Test(unittest.TestCase):

    def test(self):
        tree = Node(1)
        left = Node(3)
        mid = Node(2)
        right = Node(4)
        tree.children = [left, mid, right]
        left.children = [Node(5), Node(6)]
        s = Solution()
        actual = s.levelOrder(tree)
        expected = [
            [1],
            [3, 2, 4],
            [5, 6]
        ]
        self.assertEqual(len(expected), len(actual))
        for i in range(3):
            self.assertEqual(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
