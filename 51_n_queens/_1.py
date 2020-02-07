import unittest
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(total: int, curr: int, solution: List[str]):
            if curr == total:
                result.append(solution)
            for i in range(total):
                if self.try_position(i, total, solution):
                    row = ''.join(['Q' if j == i else '.' for j in range(total)])
                    backtrack(total, curr + 1, solution + [row])

        backtrack(n, 0, [])
        return result

    @staticmethod
    def try_position(i, n, solution):
        j = 1
        for row in reversed(solution):
            if row[i] == 'Q':
                return False
            if i - j >= 0 and row[i - j] == 'Q':
                return False
            if i + j <= n - 1 and row[i + j] == 'Q':
                return False
            j += 1
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        expected = [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],

            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ]
        self.assertEqual(sorted(expected), sorted(s.solveNQueens(4)))


if __name__ == '__main__':
    unittest.main()
