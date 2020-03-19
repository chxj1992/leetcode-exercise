import unittest
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        class Founded(Exception):
            pass

        height = len(board)
        width = len(board[0])

        def backtrack(x: int, y: int, prefix: str):
            if prefix == word:
                raise Founded()
            if x < 0 or x >= width or y < 0 or y >= height or board[y][x] == '#':
                return
            if board[y][x] == word[len(prefix)]:
                tmp = board[y][x]
                board[y][x] = '#'
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    backtrack(x + move[0], y + move[1], prefix + tmp)
                board[y][x] = tmp

        try:
            for y, row in enumerate(board):
                for x, i in enumerate(row):
                    if i == word[0]:
                        backtrack(x, y, '')
            return False
        except Founded:
            return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
        self.assertEqual(False, s.exist([["a", "b"], ["c", "d"]], "abcd"))


if __name__ == '__main__':
    unittest.main()
