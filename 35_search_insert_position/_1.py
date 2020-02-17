import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if target <= nums[start]:
            return 0
        if target > nums[end]:
            return end + 1
        while end > start + 1:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid
        return start if nums[start] == target else end


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, s.searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, s.searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    unittest.main()
