import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, s.maxProduct([-2, 0, -1]))


if __name__ == '__main__':
    unittest.main()
