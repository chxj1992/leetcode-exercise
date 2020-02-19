import unittest


class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(964176192, s.reverseBits(43261596))


if __name__ == '__main__':
    unittest.main()
