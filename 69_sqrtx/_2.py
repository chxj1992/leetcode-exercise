import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        prev, curr = 0, x
        while int(curr) != int(prev):
            prev = curr
            curr = curr / 2 + x / (2 * curr)
        return int(curr)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.mySqrt(1))
        self.assertEqual(2, s.mySqrt(4))
        self.assertEqual(2, s.mySqrt(8))


if __name__ == '__main__':
    unittest.main()
