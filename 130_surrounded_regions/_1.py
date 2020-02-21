import unittest
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(_y: int, _x: int):
            if 0 <= _y < height and 0 <= _x < width and board[_y][_x] == 'O' and (_y, _x) not in special:
                special.add((_y, _x))
                for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(_y + a, _x + b)

        special = set()
        height = len(board)
        if height == 0:
            return
        width = len(board[0])
        for y in range(height):
            for x in range(width):
                if (y == 0 or y == height - 1 or x == 0 or x == width - 1) and board[y][x] == 'O':
                    dfs(y, x)

        for y in range(height):
            for x in range(width):
                if (y, x) not in special and board[y][x] == 'O':
                    board[y][x] = 'X'


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        data = [['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']]
        expected = [['X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X'],
                    ['X', 'O', 'X', 'X']]
        s.solve(data)
        self.assertEqual(expected, data)


if __name__ == '__main__':
    unittest.main()
