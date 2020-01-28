import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        l = len(digits) - 1
        carry = 1
        while l >= 0:
            if carry and digits[l] == 9:
                digits[l] = 0
                if l == 0:
                    digits.insert(0, 1)
            elif carry:
                digits[l] += 1
                carry = 0
            l -= 1
        return digits


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([1, 2, 4], s.plusOne([1, 2, 3]))
        self.assertEqual([1], s.plusOne([0]))
        self.assertEqual([1, 0, 0, 0], s.plusOne([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
