import unittest
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        start = 1
        end = 2

        while end > start:
            s = int((start + end) * (end - start + 1) / 2)
            if s == target:
                res.append(list(range(start, end + 1)))
                start += 1
            elif s > target:
                start += 1
            else:
                end += 1
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([[2, 3, 4], [4, 5]], s.findContinuousSequence(9))
        self.assertEqual([[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]], s.findContinuousSequence(15))


if __name__ == '__main__':
    unittest.main()
