import unittest
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Time: O(nlogn)
        Space: O(n)
        Out of memory!
        """
        l = len(heights)
        if l == 0:
            return 0
        if l == 1:
            return heights[0]
        x = min(heights)
        i = heights.index(x)
        return max(x * l, self.largestRectangleArea(heights[:i]), self.largestRectangleArea(heights[i + 1:]))


class Test(unittest.TestCase):

    def test(self):
        """
        输入: [2,1,5,6,2,3]
        输出: 10
        """
        s = Solution()
        self.assertEqual(10, s.largestRectangleArea([2, 1, 5, 6, 2, 3]))


if __name__ == '__main__':
    unittest.main()
