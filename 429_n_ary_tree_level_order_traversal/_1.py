import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            row = []
            tmp_stack = []
            while stack:
                i = stack.pop(0)
                row.append(i.val)
                if i.children is not None:
                    tmp_stack += i.children
            res.append(row)
            stack = tmp_stack
        return res


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
