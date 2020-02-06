import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) // 2
        nums.sort()
        prev = nums[0]
        count = 0
        for i in nums:
            if i == prev:
                count += 1
            else:
                prev = i
                count = 1
            if count > l:
                return i


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.majorityElement([3, 2, 3]))
        self.assertEqual(2, s.majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
