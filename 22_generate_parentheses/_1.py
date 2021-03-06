import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        dp = {0: [""], 1: ["()"]}
        for i in range(2, n + 1):
            dp[i] = []
            for j in range(i):
                for before in dp[j]:
                    for after in dp[i - 1 - j]:
                        dp[i].append('(%s)%s' % (before, after))
        return dp[n]


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
