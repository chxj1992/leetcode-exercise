import unittest


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        prev, curr = 0, 1
        for i in range(2, n + 1):
            tmp = curr
            curr += prev
            prev = tmp
        return curr % 1000000007


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.fib(2))
        self.assertEqual(5, s.fib(5))


if __name__ == '__main__':
    unittest.main()
