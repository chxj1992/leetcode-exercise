import math
import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        b = "{0:b}".format(n)
        res = 1.0
        hash_map = {}
        if n > 0:
            hash_map[0] = x
        else:
            hash_map[0] = 1.0 / x
            b = b[1:]
        for i, bit in enumerate(list(reversed(b))):
            if i > 0:
                hash_map[i] = hash_map[i - 1] * hash_map[i - 1]
            if bit == '1':
                res *= hash_map[i]
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(math.pow(2.00000, 10), s.myPow(2.00000, 10))
        self.assertEqual(math.pow(2.10000, 3), s.myPow(2.10000, 3))
        self.assertEqual(math.pow(2.00000, -2), s.myPow(2.00000, -2))


if __name__ == '__main__':
    unittest.main()
