import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())


class Test(unittest.TestCase):

    def test(self):
        """
        输入: [1,2,3,4,5,6,7] 和 k = 3
        输出: [5,6,7,1,2,3,4]
        """
        nums = [1, 2, 3, 4, 5, 6, 7]
        s = Solution()
        s.rotate(nums, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums)


if __name__ == '__main__':
    unittest.main()
