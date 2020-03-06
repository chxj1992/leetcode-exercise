import unittest
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        pass


class Test(unittest.TestCase):

    def test(self):
        """
        [1,8,6,2,5,4,8,3,7]
        """
        s = Solution()
        self.assertEqual(49, s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    unittest.main()
