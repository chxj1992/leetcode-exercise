import unittest
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^3)
        Space: O(1)
        Timeout !
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = j + 1
                while k < n:
                    row = sorted([nums[i], nums[j], nums[k]])
                    if sum(row) == 0 and row not in res:
                        res.append(row)
                    k += 1
                j += 1
            i += 1
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        actual = s.threeSum(nums)
        self.assertCountEqual(expected, actual)
        for i in expected:
            self.assertIn(i, expected)

    def test2(self):
        s = Solution()
        nums = [0, 0, 0]
        expected = [
            [0, 0, 0]
        ]
        actual = s.threeSum(nums)
        self.assertCountEqual(expected, actual)
        for i in expected:
            self.assertIn(i, expected)


if __name__ == '__main__':
    unittest.main()
