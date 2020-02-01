import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        res = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    res.append('(%s)%s' % (left, right))
        return res


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
