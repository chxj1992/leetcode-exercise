import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        pass


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
