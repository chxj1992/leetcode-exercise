import unittest
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i % 2 == 1:
                res.insert(0, i)
            else:
                res.append(i)
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertIn(s.exchange([1, 2, 3, 4]), [[1, 3, 2, 4], [1, 3, 4, 2], [3, 1, 2, 4], [3, 1, 4, 2]])


if __name__ == '__main__':
    unittest.main()
