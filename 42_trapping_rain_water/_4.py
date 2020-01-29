import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        l = len(height)
        left = 0
        right = l - 1
        water = 0
        max_left = 0
        max_right = 0
        for i in range(1, l - 1):
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                water += max_left - height[left + 1] if max_left > height[left + 1] else 0
                left += 1
            else:
                max_right = max(max_right, height[right])
                water += max_right - height[right - 1] if max_right > height[right - 1] else 0
                right -= 1
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
