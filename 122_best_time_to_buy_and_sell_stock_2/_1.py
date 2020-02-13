import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(7, s.maxProfit([7, 1, 5, 3, 6, 4]))

    def test2(self):
        s = Solution()
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))

    def test3(self):
        s = Solution()
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()