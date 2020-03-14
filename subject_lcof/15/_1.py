import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n //= 2
        return count


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.hammingWeight(int('00000000000000000000000000001011', 2)))
        self.assertEqual(1, s.hammingWeight(int('00000000000000000000000010000000', 2)))
        self.assertEqual(31, s.hammingWeight(int('11111111111111111111111111111101', 2)))


if __name__ == '__main__':
    unittest.main()
