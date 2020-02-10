import unittest
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        while g and s:
            cookie = s.pop()
            child = g.pop()
            while g and cookie < child:
                child = g.pop()
            if cookie >= child:
                count += 1
        return count


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.findContentChildren([1, 2, 3], [1, 1]))
        self.assertEqual(2, s.findContentChildren([1, 2], [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
