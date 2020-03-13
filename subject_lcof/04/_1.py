import unittest
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        width, height = len(matrix[0]), len(matrix)
        x, y = 0, height - 1
        while x < width and y >= 0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                y -= 1
            else:
                x += 1
        return False


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertEqual(True, s.findNumberIn2DArray(matrix, 5))
        self.assertEqual(False, s.findNumberIn2DArray(matrix, 20))


if __name__ == '__main__':
    unittest.main()
