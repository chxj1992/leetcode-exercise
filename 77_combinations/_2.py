import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combined = list(range(1, k + 1))
        res = []
        stack = []
        while combined[0] < n + 1 - k:
            res.append(combined.copy())
            combined[-1] += 1
            while combined[-1] == n + 1 - k + len(combined):
                stack.append(combined.pop())
                combined[-1] += 1
            while stack:
                stack.pop()
                combined.append(combined[-1] + 1)
        res.append(combined)
        return res


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        expected = [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
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
