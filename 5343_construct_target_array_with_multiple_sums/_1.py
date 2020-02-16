import heapq
import unittest
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-i for i in target]
        heapq.heapify(heap)
        x = - heapq.heappop(heap)
        while x > 1:
            rest = total - x
            if rest > x or rest < 1:
                return False
            heapq.heappush(heap, - (x - rest))
            total = x
            x = -heapq.heappop(heap)
        return True


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        target = [9, 3, 5]
        self.assertEqual(True, s.isPossible(target))

    def test2(self):
        s = Solution()
        target = [1, 1, 1, 2]
        self.assertEqual(False, s.isPossible(target))

    def test3(self):
        s = Solution()
        target = [8, 5]
        self.assertEqual(True, s.isPossible(target))

    def test4(self):
        s = Solution()
        target = [9, 9, 9]
        self.assertEqual(False, s.isPossible(target))

    def test5(self):
        s = Solution()
        target = [1, 1, 1, 1, 11, 16]
        self.assertEqual(True, s.isPossible(target))

    def test6(self):
        s = Solution()
        target = [1, 1, 1, 6, 11, 16]
        self.assertEqual(False, s.isPossible(target))


if __name__ == '__main__':
    unittest.main()
