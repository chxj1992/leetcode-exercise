import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(_i, _j):
            queue = [(_i, _j)]
            while queue:
                point = queue.pop(0)
                if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]) and grid[point[0]][point[1]] == '1':
                    grid[point[0]][point[1]] = '0'
                    queue.append((point[0] + 1, point[1]))
                    queue.append((point[0], point[1] + 1))
                    queue.append((point[0] - 1, point[1]))
                    queue.append((point[0], point[1] - 1))

        count = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '1':
                    bfs(i, j)
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
