import unittest


class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n - 1)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(6, s.sumNums(3))
        self.assertEqual(45, s.sumNums(9))


if __name__ == '__main__':
    unittest.main()
