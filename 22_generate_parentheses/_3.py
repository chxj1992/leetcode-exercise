import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(_n: int, prefix: str):
            if _n == 0:
                result.append(prefix)
                return
            left_count = prefix.count('(')
            right_count = prefix.count(')')
            if left_count < n:
                backtrack(_n - 1, prefix + '(')
            if right_count < left_count:
                backtrack(_n - 1, prefix + ')')

        result = []
        backtrack(2 * n, "")
        return result


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        expected = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        self.assertEqual(sorted(expected), sorted(s.generateParenthesis(3)))


if __name__ == '__main__':
    unittest.main()
