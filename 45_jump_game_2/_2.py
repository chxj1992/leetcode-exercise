import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Timeout!
        """
        l = len(nums)
        dp_map = {l: 0}
        for n in reversed(range(1, l)):
            dp_map[n] = -1
            for i in reversed(range(1, nums[n - 1] + 1)):
                if n + i in dp_map and dp_map[n + i] >= 0:
                    dp_map[n] = min(dp_map[n], dp_map[n + i] + 1) if dp_map[n] >= 0 else dp_map[n + i] + 1
        return dp_map[1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, s.jump([2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
