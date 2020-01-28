import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        l = len(digits) - 1
        n = 0
        for i in digits:
            n += i * pow(10, l)
            l -= 1
        n += 1
        res = []
        while n > 0:
            res.insert(0, n % 10)
            n = n // 10
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([1, 2, 4], s.plusOne([1, 2, 3]))
        self.assertEqual([1], s.plusOne([0]))
        self.assertEqual([1, 0, 0, 0], s.plusOne([9, 9, 9]))
        self.assertEqual([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 4],
                         s.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))


if __name__ == '__main__':
    unittest.main()
