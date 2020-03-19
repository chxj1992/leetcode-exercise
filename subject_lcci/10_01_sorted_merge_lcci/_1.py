import unittest
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        i = 0
        while B:
            if i >= m or B[0] < A[i]:
                A.insert(i, B.pop(0))
                m += 1
                A.pop()
            i += 1


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        A = [1, 2, 3, 0, 0, 0]
        m = 3
        B = [2, 5, 6]
        n = 3
        s.merge(A, m, B, n)
        self.assertEqual([1, 2, 2, 3, 5, 6], A)

    def test2(self):
        s = Solution()
        A = [0]
        m = 0
        B = [1]
        n = 1
        s.merge(A, m, B, n)
        self.assertEqual([1], A)


if __name__ == '__main__':
    unittest.main()
