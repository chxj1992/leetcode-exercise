import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Timeout!
        """
        l = len(nums)
        dp_map = {l: True}
        for n in reversed(range(1, l)):
            dp_map[n] = False
            for i in reversed(range(1, nums[n - 1] + 1)):
                if n + i in dp_map and dp_map[n + i] is True:
                    dp_map[n] = True
                    break
        return dp_map[1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
