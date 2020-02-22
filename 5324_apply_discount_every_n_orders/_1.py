import unittest
from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products_map = {x: i for i, x in enumerate(products)}
        self.prices = prices
        self.customer_num = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_num += 1
        discount = 0
        if self.customer_num % self.n == 0:
            discount = self.discount / 100
        total = 0
        for i, p in enumerate(product):
            total += self.prices[self.products_map[p]] * (1 - discount) * amount[i]
        return total


class Test(unittest.TestCase):

    def test(self):
        cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])

        self.assertEqual(500.0, cashier.getBill([1, 2], [1, 2]))
        self.assertEqual(4000.0, cashier.getBill([3, 7], [10, 10]))
        self.assertEqual(800.0, cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(4000.0, cashier.getBill([4], [10]))
        self.assertEqual(4000.0, cashier.getBill([7, 3], [10, 10]))
        self.assertEqual(7350.0, cashier.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
        self.assertEqual(2500.0, cashier.getBill([2, 3, 5], [5, 3, 2]))


if __name__ == '__main__':
    unittest.main()
