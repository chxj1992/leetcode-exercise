import unittest
from typing import List


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        997. 找到小镇的法官
        https://leetcode-cn.com/problems/find-the-town-judge/
        """
        class NotJudge(Exception):
            pass

        relation_map = {}
        for relation in trust:
            trust_set = relation_map.setdefault(relation[0], set())
            trust_set.add(relation[1])

        judge = -1
        for i in range(1, N + 1):
            if i in relation_map:
                continue
            try:
                for trust_set in relation_map.values():
                    if i not in trust_set:
                        raise NotJudge()
                if judge != -1:
                    return -1
                judge = i
            except NotJudge:
                continue
        return judge


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(2, s.findJudge(N=2, trust=[[1, 2]]))

    def test2(self):
        s = Solution()
        self.assertEqual(3, s.findJudge(N=3, trust=[[1, 3], [2, 3]]))

    def test3(self):
        s = Solution()
        self.assertEqual(-1, s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))

    def test4(self):
        s = Solution()
        self.assertEqual(-1, s.findJudge(N=3, trust=[[1, 2], [2, 3]]))

    def test5(self):
        s = Solution()
        self.assertEqual(3, s.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))


if __name__ == '__main__':
    unittest.main()
