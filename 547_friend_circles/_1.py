import unittest
from typing import List


class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        l = count = len(M)
        p = list(range(count))

        def find_parent(i: int):
            while i != p[i]:
                i = p[i]
            return i

        def union(a: int, b: int, _count: int):
            parent_a = find_parent(a)
            parent_b = find_parent(b)
            if parent_a != parent_b:
                _count -= 1
                p[parent_a] = parent_b
            return _count

        for y in range(l):
            for x in range(y):
                if M[y][x] == 1:
                    count = union(y, x, count)

        return count


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        data = [[1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]]
        self.assertEqual(2, s.findCircleNum(data))

    def test2(self):
        s = Solution()
        data = [[1, 1, 0],
                [1, 1, 1],
                [0, 1, 1]]
        self.assertEqual(1, s.findCircleNum(data))


if __name__ == '__main__':
    unittest.main()
