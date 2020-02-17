import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class DiffPrefix(Exception):
            pass

        if not strs:
            return ''
        i = 0
        prefix = ''
        first_len = len(strs[0])
        while True:
            if i > first_len - 1:
                return prefix
            common = strs[0][i]
            try:
                for s in strs[1:]:
                    if i > len(s) - 1 or s[i] != common:
                        raise DiffPrefix()
                prefix += common
            except DiffPrefix:
                break
            i += 1
        return prefix


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual("fl", s.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual("", s.longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == '__main__':
    unittest.main()
