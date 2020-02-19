import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2
            n //= 2
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.hammingWeight(int('00000000000000000000000000001011', 2)))


if __name__ == '__main__':
    unittest.main()
