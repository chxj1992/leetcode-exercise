import unittest


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        prev, curr = num, 0
        while prev - curr > 1:
            prev = curr if curr > 0 else num
            curr = (prev + num / prev) / 2
        return int(prev) * int(prev) == num


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isPerfectSquare(16))
        self.assertEqual(False, s.isPerfectSquare(14))


if __name__ == '__main__':
    unittest.main()
