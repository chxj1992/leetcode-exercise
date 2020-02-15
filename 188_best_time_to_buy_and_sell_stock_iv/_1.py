import unittest
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n // 2:
            return self.maxProfitInf(prices)

        dp = {}
        k = min(k, n // 2 + 1)
        for i in range(-1, n):
            if i not in dp:
                dp[i] = {}
            for _k in range(k + 1):
                if _k not in dp[i]:
                    dp[i][_k] = {}
                if i == -1 or _k == 0:
                    dp[i][_k][0] = 0
                    dp[i][_k][1] = float('-infinity')
                else:
                    dp[i][_k][0] = max(dp[i - 1][_k][0], dp[i - 1][_k][1] + prices[i])
                    dp[i][_k][1] = max(dp[i - 1][_k][1], dp[i - 1][_k - 1][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfitInf(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        for i in range(-1, n):
            if i not in dp:
                dp[i] = {}
                if i == -1:
                    dp[i][0] = 0
                    dp[i][1] = float('-infinity')
                else:
                    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        # self.assertEqual(2, s.maxProfit(2, [2, 4, 1]))
        self.assertEqual(7, s.maxProfit(2, [3, 2, 6, 5, 0, 3]))


if __name__ == '__main__':
    unittest.main()
