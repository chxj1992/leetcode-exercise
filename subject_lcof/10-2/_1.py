import unittest


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 3:
            return n
        prev, curr = 2, 3
        for i in range(4, n + 1):
            tmp = curr
            curr += prev
            prev = tmp
        return curr % 1000000007


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.numWays(2))
        self.assertEqual(21, s.numWays(7))


if __name__ == '__main__':
    unittest.main()
