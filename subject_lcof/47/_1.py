import unittest
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp_map = {
            0: {0: grid[0][0]}
        }
        for y, row in enumerate(grid):
            dp_row = dp_map.setdefault(y, {})
            for x, val in enumerate(row):
                prev_row = dp_map.setdefault(y - 1, {})
                dp_row[x] = val + max(prev_row.setdefault(x, 0), dp_row.setdefault(x - 1, 0))
        return dp_map[len(grid) - 1][len(grid[0]) - 1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(12, s.maxValue([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))


if __name__ == '__main__':
    unittest.main()
