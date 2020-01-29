import unittest
from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = [-1]
        area = 0
        for i, x in enumerate(heights):
            if stack[-1] < 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
                continue
            while stack[-1] >= 0 and heights[stack[-1]] >= heights[i]:
                x = stack.pop()
                area = max(area, heights[x] * (i - stack[-1] - 1))
            stack.append(i)
        while len(stack) > 1:
            x = stack.pop()
            area = max(area, heights[x] * (len(heights) - stack[-1] - 1))
        return area


class Test(unittest.TestCase):

    def test1(self):
        """
        输入: [2,1,5,6,2,3]
        输出: 10
        """
        s = Solution()
        self.assertEqual(10, s.largestRectangleArea([2, 1, 5, 6, 2, 3]))

    def test2(self):
        """
        输入: [1]
        输出: 1
        """
        s = Solution()
        self.assertEqual(1, s.largestRectangleArea([1]))

    def test3(self):
        """
        输入: [1, 1]
        输出: 2
        """
        s = Solution()
        self.assertEqual(2, s.largestRectangleArea([1, 1]))

    def test4(self):
        """
        输入: [2, 1, 2]
        输出: 3
        """
        s = Solution()
        self.assertEqual(3, s.largestRectangleArea([2, 1, 2]))

    def test5(self):
        """
        输入: [5,4,1,2]
        输出: 8
        """
        s = Solution()
        self.assertEqual(8, s.largestRectangleArea([5, 4, 1, 2]))


if __name__ == '__main__':
    unittest.main()
