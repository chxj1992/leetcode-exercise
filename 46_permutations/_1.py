import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        while nums:
            x = nums.pop(0)
            for row in self.permute(nums):
                for i in range(len(row) + 1):
                    res.append(row[:i] + [x] + row[i:])
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
