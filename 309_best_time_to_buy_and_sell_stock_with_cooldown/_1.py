import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        for i in range(-2, n):
            if i not in dp:
                dp[i] = {}
                if i in (-2, -1):
                    dp[i][0] = 0
                    dp[i][1] = float('-infinity')
                else:
                    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                    dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[n - 1][0]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.maxProfit([1, 2, 3, 0, 2]))


if __name__ == '__main__':
    unittest.main()
