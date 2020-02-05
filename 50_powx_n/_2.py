import functools
import math
import unittest


class Solution:
    @functools.lru_cache(maxsize=256)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1.0 / x

        return self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(math.pow(2.00000, 10), s.myPow(2.00000, 10))
        self.assertEqual(math.pow(2.10000, 3), s.myPow(2.10000, 3))
        self.assertEqual(math.pow(2.00000, -2), s.myPow(2.00000, -2))


if __name__ == '__main__':
    unittest.main()
