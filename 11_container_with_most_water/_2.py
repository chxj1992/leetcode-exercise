import unittest
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return area


class Test(unittest.TestCase):

    def test(self):
        """
        [1,8,6,2,5,4,8,3,7]
        """
        s = Solution()
        self.assertEqual(49, s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    unittest.main()
