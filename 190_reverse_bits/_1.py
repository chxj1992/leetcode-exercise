import unittest


class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = '0' * (32 - len(b)) + b
        return int(b[::-1], 2)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(964176192, s.reverseBits(43261596))


if __name__ == '__main__':
    unittest.main()
