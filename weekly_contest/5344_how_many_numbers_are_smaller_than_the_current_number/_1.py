import unittest
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        for i in nums:
            res.append(sorted_nums.index(i))
        return res


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual([4, 0, 1, 1, 3], s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))

    def test2(self):
        s = Solution()
        self.assertEqual([2, 1, 0, 3], s.smallerNumbersThanCurrent([6, 5, 4, 8]))

    def test3(self):
        s = Solution()
        self.assertEqual([0, 0, 0, 0], s.smallerNumbersThanCurrent([7, 7, 7, 7]))


if __name__ == '__main__':
    unittest.main()
