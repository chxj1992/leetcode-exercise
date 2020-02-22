import unittest
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        class FoundSolution(Exception):
            pass

        def backtrack(position: int):
            if position == len(blank):
                raise FoundSolution('aha!')
            _i, _j = blank[position]
            _row_set = row_map.setdefault(_i, set())
            _column_set = column_map.setdefault(_j, set())
            _block_set = block_map.setdefault(_i // 3 * 3 + _j // 3, set())
            for test in range(1, 10):
                if test not in _row_set and test not in _column_set and test not in _block_set:
                    _row_set.add(test)
                    _column_set.add(test)
                    _block_set.add(test)
                    board[_i][_j] = str(test)
                    backtrack(position + 1)

                    # recover
                    _row_set.remove(test)
                    _column_set.remove(test)
                    _block_set.remove(test)
                    board[_i][_j] = '.'

        row_map = {}
        column_map = {}
        block_map = {}
        blank = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    row_set = row_map.setdefault(i, set())
                    column_set = column_map.setdefault(j, set())
                    block_set = block_map.setdefault(i // 3 * 3 + j // 3, set())
                    row_set.add(int(x))
                    column_set.add(int(x))
                    block_set.add(int(x))
                else:
                    blank.append((i, j))

        try:
            backtrack(0)
        except FoundSolution:
            return


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        data = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        s.solveSudoku(data)
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]
        self.assertEqual(expected, data)


if __name__ == '__main__':
    unittest.main()
