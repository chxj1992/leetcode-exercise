import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Time: O(m+n)
        Space: O(m+n)
        """
        n1 = nums1[:m]
        n2 = nums2[:n]
        res = []
        while m + n > 0:
            if len(n1) > 0 and len(n2) > 0:
                if n1[0] < n2[0]:
                    res.append(n1.pop(0))
                    m -= 1
                else:
                    res.append(n2.pop(0))
                    n -= 1
            else:
                res += n1[:m] + n2[:n]
                break

        for i, x in enumerate(res):
            nums1[i] = x


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
