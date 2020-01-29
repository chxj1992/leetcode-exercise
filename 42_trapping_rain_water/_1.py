import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time: O(n) ~ O(n^2)
        Space: O(n)
        """
        water = 0
        stack = []
        for right, x in enumerate(height):
            if len(stack) == 0 or x < height[stack[-1]]:
                stack.append(right)
                continue
            bottom = 0
            while len(stack) > 0 and x >= bottom:
                left = stack[-1]
                h = min(x, height[left])
                water += (h - bottom) * (right - left - 1)
                bottom = h
                if x >= height[left]:
                    stack.pop()
                else:
                    break
            stack.append(right)
        return water


class Test(unittest.TestCase):

    def test1(self):
        """
        输入: [0,1,0,2,1,0,1,3,2,1,2,1]
        输出: 6
        """
        s = Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test2(self):
        """
        输入: [4,2,3]
        输出: 1
        """
        s = Solution()
        self.assertEqual(1, s.trap([4, 2, 3]))

    def test3(self):
        """
        输入: [3,1,0,1,5]
        输出: 6
        """
        s = Solution()
        self.assertEqual(6, s.trap([3, 1, 0, 2, 5]))


if __name__ == '__main__':
    unittest.main()
