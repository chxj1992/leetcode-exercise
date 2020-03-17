import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                majority = i
            count = count + 1 if i == majority else count - 1
        return majority


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))


if __name__ == '__main__':
    unittest.main()
