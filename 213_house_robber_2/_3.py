import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        def _rob(_nums: List[int]) -> int:
            dp_list = [0]
            for i, x in enumerate(_nums):
                if i < 2:
                    dp_list.append(max(_nums[:i + 1]))
                else:
                    dp_list.append(max(dp_list[i], dp_list[i - 1] + x))
            return dp_list[-1]

        return max(_rob(nums[1:]), _rob(nums[:-1]))


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.rob([2, 3, 2]))
        self.assertEqual(4, s.rob([1, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
