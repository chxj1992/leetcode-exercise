import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, max_here, min_here = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            if x < 0:
                max_here, min_here = min_here, max_here
            max_here = max(max_here * x, x)
            min_here = min(min_here * x, x)
            max_product = max(max_here, max_product)
        return max_product


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, s.maxProduct([-2, 0, -1]))


if __name__ == '__main__':
    unittest.main()
