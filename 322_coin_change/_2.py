import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = min(coins)
        dp_map = {0: 0}
        for i in coins:
            dp_map[i] = 1
        for x in range(min_coin, amount + 1):
            for i in coins:
                if (x - i) in dp_map:
                    dp_map[x] = dp_map[x - i] + 1 if x not in dp_map else min(dp_map[x], dp_map[x - i] + 1)
        return dp_map[amount] if amount in dp_map else -1


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(3, s.coinChange([1, 2, 5], 11))

    def test2(self):
        s = Solution()
        self.assertEqual(-1, s.coinChange([2], 3))

    def test3(self):
        s = Solution()
        self.assertEqual(20, s.coinChange([1, 2, 5], 100))

    def test4(self):
        s = Solution()
        self.assertEqual(20, s.coinChange([186, 419, 83, 408], 6249))


if __name__ == '__main__':
    unittest.main()
