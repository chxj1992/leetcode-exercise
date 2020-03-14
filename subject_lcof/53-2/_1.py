import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        start, end = 0, len(nums) - 1
        while end > start + 1:
            mid = start + (end - start) // 2
            if nums[mid] > mid:
                end = mid - 1
            else:
                start = mid
        return nums[start] + 1 if nums[end] - nums[start] > 1 else nums[end] + 1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.missingNumber([0, 1, 3]))
        self.assertEqual(8, s.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
        self.assertEqual(2, s.missingNumber([0, 1]))


if __name__ == '__main__':
    unittest.main()
