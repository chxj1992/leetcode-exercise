import math
import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        start, end = 0, x
        while end > start + 1:
            mid = (start + end) / 2
            if mid * mid <= x:
                start = math.floor(mid)
            else:
                end = math.ceil(mid)
        return start


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.mySqrt(4))
        self.assertEqual(2, s.mySqrt(8))


if __name__ == '__main__':
    unittest.main()
