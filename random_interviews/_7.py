import math
import unittest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        633. 平方数之和
        https://leetcode-cn.com/problems/sum-of-square-numbers/
        """
        for i in range(c + 1):
            rest = c - i * i
            if rest < 0:
                break
            s = math.sqrt(rest)
            if s == int(s):
                return True
        return False


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.judgeSquareSum(0))
        self.assertEqual(True, s.judgeSquareSum(5))
        self.assertEqual(False, s.judgeSquareSum(3))


if __name__ == '__main__':
    unittest.main()
