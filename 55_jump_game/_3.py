import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_position = 1
        l = len(nums)
        for i, x in enumerate(nums):
            if i >= max_position:
                return False
            if i + x + 1 >= max_position:
                max_position = i + x + 1
                if max_position >= l:
                    return True
        return False


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 4]))
        self.assertEqual(False, s.canJump([0, 2, 3]))
        self.assertEqual(True, s.canJump([0]))


if __name__ == '__main__':
    unittest.main()
