import unittest
from typing import List

"""
33. 搜索旋转排序数组
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""


class Solution:

    def solve(self, arr: List[int], v: int) -> int:
        def binary(start, end):
            while end > start:
                mid = (start + end) // 2
                if arr[mid] == v:
                    return mid
                if arr[mid] > v:
                    start = mid
                else:
                    end = mid
            return -1

        n = len(arr)
        if n == 1:
            if arr[0] != v:
                return -1
            else:
                return 0

        m = n // 2
        if arr[m] == v:
            return m
        if arr[m] > arr[0]:
            if arr[0] <= v <= arr[m]:
                return binary(0, m)
            else:
                res = self.solve(arr[m:], v)
                return m + res if res != -1 else res
        else:
            if arr[n - 1] >= v >= arr[m]:
                return binary(m, n - 1)
            else:
                return self.solve(arr[:m], v)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(0, s.solve([8, 2, 4, 6], 8))
        self.assertEqual(1, s.solve([8, 2, 4, 6], 2))
        self.assertEqual(-1, s.solve([8, 2, 4, 6], 1))
        self.assertEqual(0, s.solve([8], 8))
        self.assertEqual(2, s.solve([8, 2, 4, 6], 4))
        self.assertEqual(4, s.solve([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, s.solve([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(1, s.solve([5, 1, 2, 3, 4], 1))


if __name__ == '__main__':
    unittest.main()
