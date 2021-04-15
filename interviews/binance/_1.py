import unittest


class Solution:
    def sqrt(self, n: int) -> float:
        x, start, end = n, 0, n
        while abs(x * x - n) > 0.001:
            x = (start + end) / 2
            if x * x == n:
                return x
            elif x * x > n:
                end = x
            else:
                start = x
        return round(x * 1000) / 1000


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        print(s.sqrt(1))
        print(s.sqrt(2))
        print(s.sqrt(4))
        print(s.sqrt(9))


if __name__ == '__main__':
    unittest.main()
