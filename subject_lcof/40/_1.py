import heapq
import unittest
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return [heapq.heappop(arr) for i in range(k)]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(sorted([1, 2]), s.getLeastNumbers([3, 2, 1], 2))
        self.assertEqual(sorted([0]), s.getLeastNumbers([0, 1, 2, 1], 1))


if __name__ == '__main__':
    unittest.main()
