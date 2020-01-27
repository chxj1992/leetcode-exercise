import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Time: O(m+n)
        Space: O(m+n)
        """
        merged = self.mergeReturn(nums1, m, nums2, n)
        for i, x in enumerate(merged):
            nums1[i] = x

    def mergeReturn(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        if m == 0:
            return nums2[:n]
        if n == 0:
            return nums1[:m]

        if nums1[0] < nums2[0]:
            return [nums1[0]] + self.mergeReturn(nums1[1:], m - 1, nums2, n)
        else:
            return [nums2[0]] + self.mergeReturn(nums1, m, nums2[1:], n - 1)


class Test(unittest.TestCase):

    def test(self):
        """
        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]
        """
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)


if __name__ == '__main__':
    unittest.main()
