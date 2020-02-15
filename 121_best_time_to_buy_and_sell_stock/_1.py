import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        prev = prices[0]
        max_profit = 0
        max_here = 0
        for t in prices[1:]:
            x = t - prev
            prev = t
            max_here = max_here + x if max_here > 0 else x
            max_profit = max(max_profit, max_here)
        return max_profit


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(5, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
