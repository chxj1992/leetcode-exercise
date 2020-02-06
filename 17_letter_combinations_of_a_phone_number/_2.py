import unittest
from typing import List


class Solution:

    def __init__(self) -> None:
        self.hash_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        if len(digits) == 1:
            return list(self.hash_map[digits[0]])
        res = []
        for x in list(self.hash_map[digits[0]]):
            for other in self.letterCombinations(digits[1:]):
                res.append(x + other)
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertCountEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
                              sorted(s.letterCombinations("23")))


if __name__ == '__main__':
    unittest.main()
