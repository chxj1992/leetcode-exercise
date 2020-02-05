import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j + 1, k - 1, tmp + [j])

        backtrack(1, k, [])
        return res


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
