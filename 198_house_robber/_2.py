import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_list = [0]
        for i, x in enumerate(nums):
            if i < 2:
                dp_list.append(max(nums[:i + 1]))
            else:
                dp_list.append(max(dp_list[i], dp_list[i - 1] + x))

        return dp_list[-1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.rob([1, 2, 3, 1]))
        self.assertEqual(12, s.rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
