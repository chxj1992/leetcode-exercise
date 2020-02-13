import functools
import unittest
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        @functools.lru_cache(maxsize=256)
        def recursion(m: int, n: int):
            x = width - n
            y = height - m
            if obstacleGrid[y][x] == 1:
                return 0
            if m == 1 and n == 1:
                return 1
            sub_paths = 0
            if m > 1 and obstacleGrid[y + 1] != 1:
                sub_paths += recursion(m - 1, n)
            if n > 1 and obstacleGrid[y][x + 1] != 1:
                sub_paths += recursion(m, n - 1)
            return sub_paths

        return recursion(height, width)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(2, s.uniquePathsWithObstacles(grid))

    def test2(self):
        s = Solution()
        grid = [[1, 0]]
        self.assertEqual(0, s.uniquePathsWithObstacles(grid))

    def test3(self):
        s = Solution()
        grid = [[0, 1]]
        self.assertEqual(0, s.uniquePathsWithObstacles(grid))

    def test4(self):
        s = Solution()
        grid = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(7, s.uniquePathsWithObstacles(grid))


if __name__ == '__main__':
    unittest.main()
