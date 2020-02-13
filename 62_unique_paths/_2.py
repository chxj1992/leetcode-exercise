import functools
import unittest


class Solution:

    def __init__(self) -> None:
        self.count = 0

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Timeout!
        """
        self.count = 0

        def backtrack(_m: int, _n: int):
            if _m == 1 or _n == 1:
                self.count += 1
                return
            backtrack(_m - 1, _n)
            backtrack(_m, _n - 1)

        backtrack(m, n)
        return self.count


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))


if __name__ == '__main__':
    unittest.main()
