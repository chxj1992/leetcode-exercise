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
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.climbStairs(100), 573147844013817084101)


if __name__ == '__main__':
    unittest.main()
