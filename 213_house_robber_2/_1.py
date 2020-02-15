import functools
import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        @functools.lru_cache(maxsize=256)
        def _rob(i: int, rob_first: bool):
            if rob_first:
                if len(nums[i:]) == 1:
                    return 0
                if len(nums[i:]) == 2:
                    return nums[i]
            else:
                if len(nums[i:]) <= 2:
                    return max(nums[i:])

            return max(nums[i] + _rob(i + 2, rob_first), _rob(i + 1, rob_first))

        return max(_rob(2, True) + nums[0], _rob(1, False))


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.rob([2, 3, 2]))
        self.assertEqual(4, s.rob([1, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
