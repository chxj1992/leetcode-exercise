import unittest
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertIn(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]), [2, 3])


if __name__ == '__main__':
    unittest.main()
