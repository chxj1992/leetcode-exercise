import unittest
from typing import List


class Solution:

    def __init__(self) -> None:
        self.hash_map = {0: 0}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.hash_map:
            return self.hash_map[amount]

        plans = []
        for i in coins:
            if amount < i:
                continue
            plan = self.coinChange(coins, amount - i)
            if plan != -1:
                plans.append(plan)

        self.hash_map[amount] = -1 if len(plans) == 0 else min(plans) + 1
        return self.hash_map[amount]


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
