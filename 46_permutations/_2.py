import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums: List[int], permute: List[int]):
            if not nums:
                res.append(permute)
                return
            for i, x in enumerate(nums):
                backtrack(nums[:i] + nums[i + 1:], permute + [x])

        backtrack(nums, [])
        return res


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        self.assertEqual(sorted(expected), sorted(s.permute([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
