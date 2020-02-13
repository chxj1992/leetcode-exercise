import unittest
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass


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
