import unittest
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp_map = {}
        for i, row in enumerate(reversed(obstacleGrid)):
            for j, x in enumerate(reversed(row)):
                if x == 1:
                    dp_map["%d-%d" % (i, j)] = 0
                elif i == 0 and j == 0:
                    dp_map["%d-%d" % (i, j)] = 1
                elif i == 0:
                    dp_map["%d-%d" % (i, j)] = dp_map["%d-%d" % (i, j - 1)]
                elif j == 0:
                    dp_map["%d-%d" % (i, j)] = dp_map["%d-%d" % (i - 1, j)]
                else:
                    dp_map["%d-%d" % (i, j)] = dp_map["%d-%d" % (i - 1, j)] + dp_map["%d-%d" % (i, j - 1)]
        return dp_map["%d-%d" % (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)]


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
