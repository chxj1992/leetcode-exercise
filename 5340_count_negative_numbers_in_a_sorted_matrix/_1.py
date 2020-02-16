import unittest
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])

        def count_neg(h: int, w: int) -> int:
            if h == 0 or w == 0:
                return 0
            start = 0
            end = w - 1
            if grid[height - h][end] >= 0:
                return count_neg(h - 1, w)
            if grid[height - h][start] < 0:
                return w * h
            while end - start > 1:
                mid = (start + end) // 2
                if grid[height - h][mid] < 0:
                    end = mid
                else:
                    start = mid
            point = start if start < 0 else end
            return (w - point) * h + count_neg(h - 1, point)

        return count_neg(height, width)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        self.assertEqual(8, s.countNegatives(grid))

    def test2(self):
        s = Solution()
        grid = [[1, -1], [-1, -1]]
        self.assertEqual(3, s.countNegatives(grid))

    def test3(self):
        s = Solution()
        grid = [[3, 2], [1, 0]]
        self.assertEqual(0, s.countNegatives(grid))

    def test4(self):
        s = Solution()
        grid = [[-1]]
        self.assertEqual(1, s.countNegatives(grid))

    def test5(self):
        s = Solution()
        grid = [[3, -1, -3, -3, -3], [2, -2, -3, -3, -3], [1, -2, -3, -3, -3], [0, -3, -3, -3, -3]]
        self.assertEqual(16, s.countNegatives(grid))


if __name__ == '__main__':
    unittest.main()
