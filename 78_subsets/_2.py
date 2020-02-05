import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]

        def backtrack(current: List[int], nums: List[int]):
            for i, x in enumerate(nums):
                newset = current + [x]
                sets.append(newset)
                backtrack(newset, nums[i + 1:])

        backtrack([], nums)
        return sets


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        self.assertEqual(sorted(expected), sorted(s.subsets([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
