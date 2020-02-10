import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_position = 0
        steps = 0
        for i in range(len(nums) - 1):
            # 找能跳的最远的
            max_position = max(max_position, nums[i] + i)
            # 遇到边界，就更新边界，并且步数加一
            if i == end:
                end = max_position
                steps += 1
        return steps


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, s.jump([2, 3, 0, 1, 4]))
        self.assertEqual(0, s.jump([1]))
        self.assertEqual(1, s.jump([2, 1]))
        self.assertEqual(2, s.jump([1, 2, 3]))
        self.assertEqual(1, s.jump([3, 2, 1]))
        self.assertEqual(1, s.jump([2, 3, 1]))
        self.assertEqual(3, s.jump([1, 1, 1, 1]))
        self.assertEqual(2, s.jump([3, 0, 2, 0, 3]))


if __name__ == '__main__':
    unittest.main()
