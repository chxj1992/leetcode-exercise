import unittest
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            wallet[bill] += 1
            if bill == 10:
                if wallet[5] >= 1:
                    wallet[5] -= 1
                else:
                    return False
            if bill == 20:
                if wallet[10] >= 1 and wallet[5] >= 1:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.lemonadeChange([5, 5, 5, 10, 20]))
        self.assertEqual(True, s.lemonadeChange([5, 5, 10]))
        self.assertEqual(False, s.lemonadeChange([10, 10]))
        self.assertEqual(False, s.lemonadeChange([5, 5, 10, 10, 20]))


if __name__ == '__main__':
    unittest.main()
