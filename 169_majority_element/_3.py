import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count = 1
        candidate = nums[0]
        for i in nums[1:]:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1

        return candidate


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.majorityElement([3, 2, 3]))
        self.assertEqual(2, s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(9, s.majorityElement([10, 9, 9, 9, 10]))


if __name__ == '__main__':
    unittest.main()
