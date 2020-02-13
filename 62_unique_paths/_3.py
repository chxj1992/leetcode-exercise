import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_map = {}
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i not in dp_map:
                    dp_map[i] = {}
                if i == 1 or j == 1:
                    dp_map[i][j] = 1
                else:
                    dp_map[i][j] = dp_map[i-1][j] + dp_map[i][j - 1]
        return dp_map[m][n]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))


if __name__ == '__main__':
    unittest.main()
