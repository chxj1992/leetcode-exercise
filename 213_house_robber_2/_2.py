import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp_map = {}
        for i, x in enumerate(nums[:-1]):
            if i == 0:
                dp_map['%d-%d' % (i, 0)] = 0
                dp_map['%d-%d' % (i, 1)] = x
            elif i == 1:
                dp_map['%d-%d' % (i, 0)] = x
                dp_map['%d-%d' % (i, 1)] = nums[0]
            else:
                dp_map['%d-%d' % (i, 0)] = max(x + dp_map['%d-%d' % (i - 2, 0)], dp_map['%d-%d' % (i - 1, 0)])
                dp_map['%d-%d' % (i, 1)] = max(x + dp_map['%d-%d' % (i - 2, 1)], dp_map['%d-%d' % (i - 1, 1)])

        return max(dp_map['%d-%d' % (n - 3, 0)] + nums[-1], dp_map['%d-%d' % (n - 2, 1)], dp_map['%d-%d' % (n - 2, 0)])


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.rob([2, 3, 2]))
        self.assertEqual(4, s.rob([1, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
