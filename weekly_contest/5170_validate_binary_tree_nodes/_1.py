import unittest
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        count = 0
        for i in range(n):
            if leftChild[i] == -1:
                count += 1
            if rightChild[i] == -1:
                count += 1
        return count == n + 1


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


if __name__ == '__main__':
    unittest.main()
