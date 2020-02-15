import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        n = len(prices)
        for i in range(-1, n):
            if i not in dp:
                dp[i] = {}
                if i == -1:
                    dp[i][0] = 0
                    dp[i][1] = float('-infinity')
                else:
                    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
                    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(8, s.maxProfit([1, 3, 2, 8, 4, 9], 2))


if __name__ == '__main__':
    unittest.main()
