import unittest
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def dfs(start: tuple, curr: tuple, length: int) -> int:
            if curr[1] >= len(matrix) or curr[0] >= len(matrix[0]):
                return length

            for _x in range(start[0], curr[0] + 1):
                if matrix[curr[1]][_x] == '0':
                    return length

            for _y in range(start[1], curr[1] + 1):
                if matrix[_y][curr[0]] == '0':
                    return length
            return dfs(start, (curr[0] + 1, curr[1] + 1), length + 1)

        max_len = 0
        for y, row in enumerate(matrix):
            for x, i in enumerate(row):
                max_len = max(max_len, dfs((x, y), (x, y), 0))
        return max_len * max_len


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        m = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0'],
        ]
        self.assertEqual(4, s.maximalSquare(m))

    def test2(self):
        s = Solution()
        m = [
            ['0', '1'],

        ]
        self.assertEqual(1, s.maximalSquare(m))


if __name__ == '__main__':
    unittest.main()
