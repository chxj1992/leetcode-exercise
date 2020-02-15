import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
