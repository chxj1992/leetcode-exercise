import unittest
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Timeout!
        """
        def exists(p):
            return 0 <= p[0] < len(board) and 0 <= p[1] < len(board[0])

        def bfs(y, x):
            queue = [(y, x)]
            while queue:
                count = 0
                point = queue.pop(0)
                positions = [(point[0] - 1, point[1] - 1),
                             (point[0] - 1, point[1]),
                             (point[0] - 1, point[1] + 1),
                             (point[0], point[1] - 1),
                             (point[0], point[1] + 1),
                             (point[0] + 1, point[1] - 1),
                             (point[0] + 1, point[1]),
                             (point[0] + 1, point[1] + 1)]
                for p in positions:
                    if exists(p) and board[p[0]][p[1]] == 'M':
                        count += 1
                if count > 0:
                    board[point[0]][point[1]] = str(count)
                else:
                    board[point[0]][point[1]] = 'B'
                    for p in positions:
                        if exists(p) and board[p[0]][p[1]] == 'E':
                            queue.append(p)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            bfs(click[0], click[1])
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
