import functools
import unittest
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)

        @functools.lru_cache(maxsize=1024)
        def min_total(y: int, x: int):
            if y + 1 > height:
                return 0
            return triangle[y][x] + min(min_total(y + 1, x), min_total(y + 1, x + 1))

        return min_total(0, 0)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
        self.assertEqual(11, s.minimumTotal(triangle))


if __name__ == '__main__':
    unittest.main()
