import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(_i, _j):
            if 0 <= _i < len(grid) and 0 <= _j < len(grid[0]):
                if grid[_i][_j] == '1':
                    grid[_i][_j] = '0'
                    dfs(_i + 1, _j)
                    dfs(_i, _j + 1)
                    dfs(_i - 1, _j)
                    dfs(_i, _j - 1)

        count = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '1':
                    dfs(i, j)
                    count += 1
        return count


class Test(unittest.TestCase):

    def test1(self):
        data = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ]

        s = Solution()
        self.assertEqual(1, s.numIslands(data))

    def test2(self):
        data = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ]

        s = Solution()
        self.assertEqual(3, s.numIslands(data))


if __name__ == '__main__':
    unittest.main()
