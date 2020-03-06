import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, s.maxSubArray([-2, -1]))


if __name__ == '__main__':
    unittest.main()
