import math
import unittest
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        n = int(math.sqrt(num + 2))
        while n > 0:
            if (num + 1) % n == 0:
                return [(num + 1) // n, n]
            if (num + 2) % n == 0:
                return [(num + 2) // n, n]
            n -= 1


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(sorted([3, 3]), sorted(s.closestDivisors(8)))

    def test2(self):
        s = Solution()
        self.assertEqual(sorted([5, 25]), sorted(s.closestDivisors(123)))

    def test3(self):
        s = Solution()
        self.assertEqual(sorted([40, 25]), sorted(s.closestDivisors(999)))


if __name__ == '__main__':
    unittest.main()
