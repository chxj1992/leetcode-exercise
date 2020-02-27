import unittest
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        种花问题
        https://leetcode-cn.com/problems/can-place-flowers/
        """
        l = len(flowerbed)

        def recursion(start: int, _n: int):
            if _n == 0:
                return True
            elif start == l:
                return False

            if flowerbed[start] == 1 or (start > 0 and flowerbed[start - 1] == 1) or (
                    start < l - 1 and flowerbed[start + 1] == 1):
                return recursion(start + 1, _n)
            else:
                flowerbed[start] = 1
                return recursion(start + 1, _n - 1)

        return recursion(0, n)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertEqual(False, s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertEqual(False, s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
        self.assertEqual(True, s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
        self.assertEqual(False, s.canPlaceFlowers([0, 1, 0, 0, 0, 0, 1], 2))
        self.assertEqual(False, s.canPlaceFlowers([0, 1, 0, 0, 0, 0, 1, 0], 2))
        self.assertEqual(True, s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1, 0], 2))
        self.assertEqual(True, s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))


if __name__ == '__main__':
    unittest.main()
