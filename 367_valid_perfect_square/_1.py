import math
import unittest


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        start, end = 0, num
        while end > start + 1:
            mid = (start + end) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = math.ceil(mid)
            else:
                start = math.floor(mid)

        return False


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isPerfectSquare(16))
        self.assertEqual(False, s.isPerfectSquare(14))


if __name__ == '__main__':
    unittest.main()
