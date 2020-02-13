import unittest
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        dp_map = {}
        for i in range(height):
            for j in range(height - i):
                if i == 0:
                    dp_map['%d-%d' % (i, j)] = triangle[height - i - 1][j]
                else:
                    dp_map['%d-%d' % (i, j)] = triangle[height - i - 1][j] + min(dp_map['%d-%d' % (i - 1, j)],
                                                                                 dp_map['%d-%d' % (i - 1, j + 1)])
        return dp_map['%d-%d' % (height - 1, 0)]


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
