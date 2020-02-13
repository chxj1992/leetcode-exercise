import functools
import unittest


class Solution:
    @functools.lru_cache(maxsize=256)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))


if __name__ == '__main__':
    unittest.main()
