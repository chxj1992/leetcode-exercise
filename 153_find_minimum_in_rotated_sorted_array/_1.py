import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                return nums[i + 1]
        return nums[0]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, s.findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(1, s.findMin([2, 3, 4, 5, 1]))


if __name__ == '__main__':
    unittest.main()
