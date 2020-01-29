import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        l = len(height)

        max_left_map = {0: 0}
        for i in range(1, l):
            max_left_map[i] = max(height[i - 1], max_left_map[i - 1])

        max_right_map = {l - 1: 0}
        for i in reversed(range(l - 1)):
            max_right_map[i] = max(height[i + 1], max_right_map[i + 1])

        water = 0
        for i, x in enumerate(height):
            limit = min(max_left_map[i], max_right_map[i])
            water += limit - x if limit > x else 0
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
