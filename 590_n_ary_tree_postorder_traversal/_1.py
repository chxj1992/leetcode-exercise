import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []
        res = []
        if root.children is not None:
            for node in root.children:
                res += self.postorder(node)
        res += [root.val]
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
        self.assertEqual([5, 6, 3, 2, 4, 1], s.postorder(tree))


if __name__ == '__main__':
    unittest.main()
