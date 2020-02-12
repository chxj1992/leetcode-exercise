import unittest


class Solution:

    def climbStairs(self, n: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        curr_step = 1
        next_step = 2
        for i in range(1, n):
            tmp = curr_step
            curr_step = next_step
            next_step = tmp + curr_step
        return curr_step


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(3, s.climbStairs(3))
        self.assertEqual(573147844013817084101, s.climbStairs(100))


if __name__ == '__main__':
    unittest.main()
