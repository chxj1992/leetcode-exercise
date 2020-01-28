import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        return [int(x) for x in list(str(int(''.join([str(x) for x in digits])) + 1))]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([1, 2, 4], s.plusOne([1, 2, 3]))
        self.assertEqual([1], s.plusOne([0]))
        self.assertEqual([1, 0, 0, 0], s.plusOne([9, 9, 9]))


if __name__ == '__main__':
    unittest.main()
