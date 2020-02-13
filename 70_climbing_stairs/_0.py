import unittest


class Solution:

    def climbStairs(self, n: int) -> int:
        pass


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))
        self.assertEqual(573147844013817084101, s.climbStairs(100))


if __name__ == '__main__':
    unittest.main()
