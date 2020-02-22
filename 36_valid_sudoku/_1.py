import unittest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        column_map = {}
        block_map = {}
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    row_set = row_map.setdefault(i, set())
                    column_set = column_map.setdefault(j, set())
                    block_set = block_map.setdefault(i // 3 * 3 + j // 3, set())
                    if x in row_set or x in column_set or x in block_set:
                        return False
                    row_set.add(x)
                    column_set.add(x)
                    block_set.add(x)
        return True


class Test(unittest.TestCase):

    def test1(self):
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
        self.assertEqual(True, s.isValidSudoku(data))

    def test2(self):
        s = Solution()
        data = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertEqual(False, s.isValidSudoku(data))


if __name__ == '__main__':
    unittest.main()
