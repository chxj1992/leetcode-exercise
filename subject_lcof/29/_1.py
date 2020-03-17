import unittest

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        curr = (0, 0)
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = [matrix[0][0]]
        while right >= left or bottom >= top:
            for step in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                while left <= curr[0] + step[0] <= right and top <= curr[1] + step[1] <= bottom:
                    curr = (curr[0] + step[0], curr[1] + step[1])
                    res.append(matrix[curr[1]][curr[0]])
                if step == (1, 0):
                    top += 1
                elif step == (0, 1):
                    right -= 1
                elif step == (-1, 0):
                    bottom -= 1
                else:
                    left += 1
        return res


class Test(unittest.TestCase):

    def test(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        s = Solution()
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], s.spiralOrder(matrix))


if __name__ == '__main__':
    unittest.main()
