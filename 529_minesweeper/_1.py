import unittest
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def exists(p):
            return 0 <= p[0] < len(board) and 0 <= p[1] < len(board[0])

        def dfs(y, x):
            if board[y][x] != 'E':
                return
            count = 0
            positions = [(y - 1, x - 1),
                         (y - 1, x),
                         (y - 1, x + 1),
                         (y, x - 1),
                         (y, x + 1),
                         (y + 1, x - 1),
                         (y + 1, x),
                         (y + 1, x + 1)]
            for p in positions:
                if exists(p) and board[p[0]][p[1]] == 'M':
                    count += 1
            if count > 0:
                board[y][x] = str(count)
            else:
                board[y][x] = 'B'
                for p in positions:
                    if exists(p):
                        dfs(p[0], p[1])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])
        return board


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        data = [['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E']]

        expected = [['B', '1', 'E', '1', 'B'],
                    ['B', '1', 'M', '1', 'B'],
                    ['B', '1', '1', '1', 'B'],
                    ['B', 'B', 'B', 'B', 'B']]

        self.assertEqual(expected, s.updateBoard(data, [3, 0]))

    def test2(self):
        s = Solution()
        data = [['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']]

        expected = [['B', '1', 'E', '1', 'B'],
                    ['B', '1', 'X', '1', 'B'],
                    ['B', '1', '1', '1', 'B'],
                    ['B', 'B', 'B', 'B', 'B']]

        self.assertEqual(expected, s.updateBoard(data, [1, 2]))


if __name__ == '__main__':
    unittest.main()
