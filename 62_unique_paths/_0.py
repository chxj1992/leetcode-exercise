import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))


if __name__ == '__main__':
    unittest.main()
