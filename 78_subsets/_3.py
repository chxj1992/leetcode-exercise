import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for i in nums:
            sets += [row + [i] for row in sets]
        return sets


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        self.assertEqual(sorted(expected), sorted(s.subsets([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
