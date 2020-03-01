import functools
import unittest
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        l = len(votes[0])
        count = {}
        for vote in votes:
            for i, char in enumerate(vote):
                s = count.setdefault(char, {})
                s[i] = s.setdefault(i, 0) + 1

        count_list = list(count.items())

        def cmp(t1: dict, t2: dict):
            for i in range(l):
                ai = t1[1].setdefault(i, 0)
                bi = t2[1].setdefault(i, 0)
                if ai > bi:
                    return -1
                if ai < bi:
                    return 1
            return 1 if t1[0] > t2[0] else -1

        count_list.sort(key=functools.cmp_to_key(cmp))

        return ''.join([k for (k, v) in count_list])


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual("ACB", s.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))

    def test2(self):
        s = Solution()
        self.assertEqual("XWYZ", s.rankTeams(["WXYZ", "XYZW"]))

    def test3(self):
        s = Solution()
        self.assertEqual("ZMNAGUEDSJYLBOPHRQICWFXTVK", s.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))

    def test4(self):
        s = Solution()
        self.assertEqual("ABC", s.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))

    def test5(self):
        s = Solution()
        self.assertEqual("M", s.rankTeams(["M", "M", "M", "M"]))


if __name__ == '__main__':
    unittest.main()
