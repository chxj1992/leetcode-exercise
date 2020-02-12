import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if end == 0:
            return 0 if nums[0] == target else -1
        while end > start:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if nums[mid] > nums[start]:
                if nums[start] < target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(1, s.search([5, 1, 2, 3, 4], 1))


if __name__ == '__main__':
    unittest.main()
