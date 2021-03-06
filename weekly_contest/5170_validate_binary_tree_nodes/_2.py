import unittest
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree_set = set()
        for i in range(n):
            in_degree = [x for x in [leftChild[i], rightChild[i]] if x != -1]
            if (i != 0 and i not in in_degree_set) or 0 in in_degree or in_degree_set.intersection(in_degree):
                return False
            in_degree_set = in_degree_set.union(in_degree)
        return True


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))

    def test2(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))

    def test3(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(2, [1, 0], [-1, -1]))

    def test4(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))

    def test5(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(5, [4, -1, 3, -1, -1], [1, 2, -1, -1, -1]))

    def test6(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(5, [1, 3, -1, -1, -1], [-1, 2, 4, -1, -1]))


if __name__ == '__main__':
    unittest.main()
