import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_here, max_so_far = nums[0], nums[0]
        for i in nums[1:]:
            max_here = max_here + i if max_here > 0 else i
            max_so_far = max(max_here, max_so_far)
        return max_so_far


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    unittest.main()
