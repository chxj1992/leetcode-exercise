import unittest
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(n^2)
        Space: O(1)
        Timeout !
        """
        area = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1:]):
                tmp = min(h1, h2) * (j + 1)
                if tmp > area:
                    area = tmp
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
