import unittest

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


class Test(unittest.TestCase):

    def test(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        s = Solution()
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], s.spiralOrder(matrix))


if __name__ == '__main__':
    unittest.main()
