import functools
import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        @functools.lru_cache(maxsize=256)
        def _rob(i: int):
            if len(nums[i:]) <= 2:
                return max(nums[i:])
            return max(nums[i] + _rob(i + 2), _rob(i + 1))

        return _rob(0)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.rob([1, 2, 3, 1]))
        self.assertEqual(12, s.rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
