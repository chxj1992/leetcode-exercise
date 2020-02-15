import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_point, total, max_sum = 0, 0, nums[0]
        for i in nums:
            total += i
            if total < min_point:
                max_sum = max(max_sum, total - min_point)
                min_point = total
            else:
                max_sum = max(max_sum, total - min_point)
        return max_sum


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(-1, s.maxSubArray([-2, -1]))
        self.assertEqual(3, s.maxSubArray([1, 2]))


if __name__ == '__main__':
    unittest.main()
