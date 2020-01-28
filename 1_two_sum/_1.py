import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n^2)
        Space: O(1)
        """
        for i, x1 in enumerate(nums):
            for j, x2 in enumerate(nums[i + 1:]):
                if x1 + x2 == target:
                    return [i, i + j + 1]


class Test(unittest.TestCase):

    def test(self):
        """
        给定 nums = [2, 7, 11, 15], target = 9
        因为 nums[0] + nums[1] = 2 + 7 = 9
        所以返回 [0, 1]
        """
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
