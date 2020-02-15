import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        for i in range(-1, n):
            if i not in dp:
                dp[i] = {}
            for k in range(3):
                if k not in dp[i]:
                    dp[i][k] = {}
                if i == -1 or k == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-infinity')
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][2][0]


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(6, s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))

    def test2(self):
        s = Solution()
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))

    def test3(self):
        s = Solution()
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
