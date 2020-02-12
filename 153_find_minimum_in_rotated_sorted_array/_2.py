import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return nums[0] if nums[1] > nums[0] else nums[1]
        mid = l // 2
        if nums[mid] > nums[-1]:
            return self.findMin(nums[mid + 1:])
        else:
            return self.findMin(nums[:mid + 1])


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, s.findMin([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(1, s.findMin([2, 3, 4, 5, 1]))


if __name__ == '__main__':
    unittest.main()
