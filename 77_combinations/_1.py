import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def _combine(nlist: List[int], k: int):
            res = []
            if k == 1:
                return [[i] for i in nlist]
            for i, x in enumerate(nlist):
                if i + k > len(nlist):
                    break
                for row in _combine(nlist[i + 1:], k - 1):
                    row.insert(0, int(x))
                    res.append(row)
            return res

        return _combine(list(range(1, n + 1)), k)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        expected = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        self.assertEqual(sorted(expected), sorted(s.combine(4, 2)))

    def test2(self):
        s = Solution()
        expected = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        self.assertEqual(sorted(expected), sorted(s.combine(4, 3)))

    def test3(self):
        s = Solution()
        expected = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
        self.assertEqual(sorted(expected), sorted(s.combine(5, 4)))


if __name__ == '__main__':
    unittest.main()
