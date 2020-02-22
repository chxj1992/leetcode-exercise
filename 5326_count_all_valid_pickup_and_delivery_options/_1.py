import functools
import unittest


class Solution:
    def countOrders(self, n: int) -> int:
        @functools.lru_cache(maxsize=1000)
        def backtrack(delivery: int, pickup: int, count: int) -> int:
            if delivery == n and pickup == n - 1:
                return 1
            add = 0
            if delivery < n:
                add += (n - delivery) * backtrack(delivery + 1, pickup, count)
            if pickup < delivery:
                add += (delivery - pickup) * backtrack(delivery, pickup + 1, count)
            return (count + add) % (10 ** 9 + 7)

        return backtrack(0, 0, 0)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(1, s.countOrders(1))
        self.assertEqual(6, s.countOrders(2))
        self.assertEqual(90, s.countOrders(3))


if __name__ == '__main__':
    unittest.main()
