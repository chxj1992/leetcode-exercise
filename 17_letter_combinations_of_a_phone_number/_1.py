import unittest
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        hash_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def backtrack(digit: str, prev: str):
            if digit == "":
                res.append(prev)
                return
            for x in hash_map[digit[0]]:
                backtrack(digit[1:], prev + x)

        backtrack(digits, "")
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertCountEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
                              sorted(s.letterCombinations("23")))


if __name__ == '__main__':
    unittest.main()
