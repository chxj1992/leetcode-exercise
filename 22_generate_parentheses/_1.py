import unittest
from typing import List


class Solution:

    def __init__(self) -> None:
        self.hash_map = {}

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 1:
            return ["()"]
        for i in self.generateParenthesis(n - 1):
            if "()" + i not in self.hash_map:
                self.hash_map["()" + i] = True
                res.append("()" + i)
            if "(" + i + ")" not in self.hash_map:
                self.hash_map["(" + i + ")"] = True
                res.append("(" + i + ")")
            if i + "()" not in self.hash_map:
                self.hash_map[i + "()"] = True
                res.append(i + "()")
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
