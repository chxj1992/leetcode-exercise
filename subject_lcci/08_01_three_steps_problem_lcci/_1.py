import unittest


class Solution:
    def waysToStep(self, n: int) -> int:
        dp_map = {1: 1, 2: 2, 3: 4}
        for i in range(4, n + 1):
            dp_map[i] = (dp_map[i - 1] + dp_map[i - 2] + dp_map[i - 3]) % 1000000007
            del dp_map[i - 3]
        return dp_map[n]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(4, s.waysToStep(3))
        self.assertEqual(13, s.waysToStep(5))


if __name__ == '__main__':
    unittest.main()
