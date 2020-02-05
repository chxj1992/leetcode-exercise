import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        x = nums.pop()
        subsets = self.subsets(nums)
        newsets = []
        for one in subsets:
            newsets.append(one + [x])
        return subsets + newsets


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        self.assertEqual(sorted(expected), sorted(s.subsets([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
