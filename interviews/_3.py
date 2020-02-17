import functools
import unittest
from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        strset = set()

        @functools.lru_cache(maxsize=1000)
        def simplify(s: str):
            odd = sorted([x for i, x in enumerate(s) if i % 2 == 1])
            even = sorted([x for i, x in enumerate(s) if i % 2 == 0])
            ol = len(odd)
            el = len(even)
            res = ""
            for i in range(ol + 2):
                if i < el:
                    res += even[i]
                if i < ol:
                    res += odd[i]
            return res

        for a in A:
            s = simplify(a)
            if s not in strset:
                strset.add(s)
        return len(strset)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(3, s.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))

    def test2(self):
        s = Solution()
        self.assertEqual(4, s.numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))

    def test3(self):
        s = Solution()
        self.assertEqual(3, s.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))

    def test4(self):
        s = Solution()
        self.assertEqual(1, s.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))


if __name__ == '__main__':
    unittest.main()
