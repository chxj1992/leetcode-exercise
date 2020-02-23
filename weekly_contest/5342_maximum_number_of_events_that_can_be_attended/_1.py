import unittest
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        attended = set()
        for e in events:
            for i in range(e[0], e[1] + 1):
                if i not in attended:
                    attended.add(i)
                    break
        return len(attended)


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        events = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(3, s.maxEvents(events))

    def test2(self):
        s = Solution()
        events = [[1, 2], [2, 3], [3, 4], [1, 2]]
        self.assertEqual(4, s.maxEvents(events))

    def test3(self):
        s = Solution()
        events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
        self.assertEqual(4, s.maxEvents(events))

    def test4(self):
        s = Solution()
        events = [[1, 100000]]
        self.assertEqual(1, s.maxEvents(events))

    def test5(self):
        s = Solution()
        events = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
        self.assertEqual(7, s.maxEvents(events))


if __name__ == '__main__':
    unittest.main()
