import unittest
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums: List[int], permute: List[int]):
            if not nums:
                res.append(permute)
                return
            prev = None
            for i, x in enumerate(nums):
                if x == prev:
                    continue
                backtrack(nums[:i] + nums[i + 1:], permute + [x])
                prev = x

        backtrack(sorted(nums), [])
        return res


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
