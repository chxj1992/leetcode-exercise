import unittest
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = {}

        def backtrack(nums: List[int], permute: List[int]):
            if not nums:
                res[','.join([str(x) for x in permute])] = permute
                return
            for i, x in enumerate(nums):
                backtrack(nums[:i] + nums[i + 1:], permute + [x])

        backtrack(nums, [])
        return res.values()


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        expected = [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ]
        self.assertEqual(sorted(expected), sorted(s.permuteUnique([1, 1, 2])))


if __name__ == '__main__':
    unittest.main()
