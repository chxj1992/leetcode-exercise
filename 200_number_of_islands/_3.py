import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        def find_parent(key: str):
            while key != p[key]:
                key = p[key]
            return key

        def union(a: str, b: str, _count: int):
            parent_a = find_parent(a)
            parent_b = find_parent(b)
            if parent_a != parent_b:
                _count -= 1
                p[parent_a] = parent_b
            return _count

        p = {}
        height = len(grid)
        width = len(grid[0])
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    count += 1
                p[str(i) + '-' + str(j)] = str(i) + '-' + str(j)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                for (x, y) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if 0 <= i + y < height and 0 <= j + x < width and grid[i][j] == '1' and grid[i + y][j + x] == '1':
                        count = union(str(i) + '-' + str(j), str(i + y) + '-' + str(j + x), count)
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
