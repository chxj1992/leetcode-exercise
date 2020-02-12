import functools
import unittest


class Solution:

    @functools.lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))
        self.assertEqual(573147844013817084101, s.climbStairs(100))


if __name__ == '__main__':
    unittest.main()
