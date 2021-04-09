import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high, max_profit = 0, 0, 0
        for i, v in enumerate(prices[1:]):
            if v < prices[low]:
                low = i + 1
                high = i + 1
            if v > prices[high]:
                high = i + 1
            max_profit = max(max_profit, prices[high] - prices[low])
        return max_profit


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
