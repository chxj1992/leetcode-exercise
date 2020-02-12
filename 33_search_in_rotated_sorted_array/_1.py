import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, x in enumerate(nums):
            if x == target:
                return i
        return -1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()
