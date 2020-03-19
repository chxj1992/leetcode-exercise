import unittest
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])

        queue = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 2:
                    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        next_x = x + move[0]
                        next_y = y + move[1]
                        if 0 <= next_x < width and 0 <= next_y < height and grid[next_y][next_x] == 1:
                            queue.append((next_x, next_y, 1))
        max_time = 0
        while queue:
            next_level = []
            while queue:
                (x, y, time) = queue.pop(0)
                if grid[y][x] != 1:
                    continue
                grid[y][x] = 2
                max_time = max(max_time, time)
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x = x + move[0]
                    next_y = y + move[1]
                    if 0 <= next_x < width and 0 <= next_y < height and grid[next_y][next_x] == 1:
                        next_level.append((next_x, next_y, time + 1))
            queue = next_level

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    return -1
        return max_time


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(4, s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

    def test2(self):
        s = Solution()
        self.assertEqual(-1, s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))

    def test3(self):
        s = Solution()
        self.assertEqual(0, s.orangesRotting([[0, 2]]))

    def test4(self):
        s = Solution()
        self.assertEqual(1, s.orangesRotting([[2, 2], [1, 1], [0, 0], [2, 0]]))


if __name__ == '__main__':
    unittest.main()
