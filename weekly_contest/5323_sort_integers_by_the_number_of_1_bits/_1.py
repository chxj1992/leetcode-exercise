import unittest
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        first = arr[0]
        first_count = bin(first).count('1')
        left = []
        right = []

        for x in arr[1:]:
            if bin(x).count('1') < first_count or (bin(x).count('1') == first_count and x < first):
                left.append(x)
            else:
                right.append(x)
        return self.sortByBits(left) + [first] + self.sortByBits(right)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual([0, 1, 2, 4, 8, 3, 5, 6, 7], s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    def test2(self):
        s = Solution()
        self.assertEqual([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
                         s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))

    def test3(self):
        s = Solution()
        self.assertEqual([10000, 10000], s.sortByBits([10000, 10000]))

    def test4(self):
        s = Solution()
        self.assertEqual([2, 3, 5, 17, 7, 11, 13, 19], s.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))

    def test5(self):
        s = Solution()
        self.assertEqual([10, 100, 10000, 1000], s.sortByBits([10, 100, 1000, 10000]))


if __name__ == '__main__':
    unittest.main()
