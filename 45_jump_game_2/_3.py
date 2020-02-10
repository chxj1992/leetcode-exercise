import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Timeout!
        """
        position = len(nums)
        steps = 0
        while position > 1:
            for i, x in enumerate(nums[:position]):
                if i + x >= position - 1:
                    position = i + 1
                    steps += 1
                    break
        return steps


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, s.jump([2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
