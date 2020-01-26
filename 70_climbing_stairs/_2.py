import unittest


class Solution:

    def climbStairs(self, n: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        if n <= 2:
            return n

        res, prev2, prev1 = 0, 1, 2
        for i in range(2, n):
            res = prev1 + prev2
            prev2 = prev1
            prev1 = res
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.climbStairs(100), 573147844013817084101)


if __name__ == '__main__':
    unittest.main()
