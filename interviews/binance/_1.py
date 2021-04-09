import unittest
from typing import List


class Solution:
    def solve(self, input: List[int]) -> bool:
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.solve([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
