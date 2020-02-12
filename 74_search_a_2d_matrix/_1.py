import unittest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        start = 0
        end = len(matrix) - 1
        while end - start > 1:
            mid = (start + end) // 2
            if matrix[mid][0] <= target:
                start = mid
            else:
                end = mid - 1
        row = matrix[start] if matrix[end][0] > target else matrix[end]
        start = 0
        end = len(row) - 1
        while end - start > 1:
            mid = (start + end) // 2
            if row[mid] > target:
                end = mid - 1
            else:
                start = mid
        return row[start] == target or row[end] == target


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        self.assertEqual(True, s.searchMatrix(matrix, target))

    def test2(self):
        s = Solution()
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13
        self.assertEqual(False, s.searchMatrix(matrix, target))

    def test3(self):
        s = Solution()
        matrix = [
        ]
        target = 0
        self.assertEqual(False, s.searchMatrix(matrix, target))

    def test4(self):
        s = Solution()
        matrix = [
            [1, 3]
        ]
        target = 3
        self.assertEqual(True, s.searchMatrix(matrix, target))


if __name__ == '__main__':
    unittest.main()
