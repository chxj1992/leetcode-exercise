import unittest
from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.last_zero_i = -1
        self.last_i = -1
        self.multiples: List[int] = [1]

    def add(self, num: int) -> None:
        self.last_i += 1
        if num == 0:
            self.last_zero_i = self.last_i
            self.multiples.append(self.multiples[-1])
        else:
            self.multiples.append(self.multiples[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.last_zero_i >= 0 and self.last_i - self.last_zero_i + 1 <= k:
            return 0
        return self.multiples[-1] // self.multiples[self.last_i - k + 1]


class Test(unittest.TestCase):

    def test(self):
        p = ProductOfNumbers()
        p.add(3)
        p.add(0)
        p.add(2)
        p.add(5)
        p.add(4)
        self.assertEqual(20, p.getProduct(2))
        self.assertEqual(40, p.getProduct(3))
        self.assertEqual(0, p.getProduct(4))
        p.add(8)
        self.assertEqual(32, p.getProduct(2))


if __name__ == '__main__':
    unittest.main()
