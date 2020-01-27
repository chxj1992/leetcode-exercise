import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Time: O(m*n)
        Space: O(1)
        """
        last = m
        for i in range(n):
            if m == 0:
                nums1.insert(last, nums2[i])
                last += 1
                nums1.pop()
                continue
            for j in range(last):
                if nums1[j] >= nums2[i]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    last += 1
                    break
                elif j == last - 1:
                    nums1.insert(last, nums2[i])
                    last += 1
                    nums1.pop()


class Test(unittest.TestCase):

    def test1(self):
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

    def test2(self):
        """
        输入:
        nums1 = [0], m = 0
        nums2 = [1],       n = 1

        输出: [1]
        """
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertEqual([1], nums1)

    def test3(self):
        """
        [4,0,0,0,0,0]
        1
        [1,2,3,5,6]
        5
        """
        nums1 = [4, 0, 0, 0, 0, 0]
        m = 1
        nums2 = [1, 2, 3, 5, 6]
        n = 5
        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 3, 4, 5, 6], nums1)


if __name__ == '__main__':
    unittest.main()
