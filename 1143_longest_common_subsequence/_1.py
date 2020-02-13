import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_map = {}
        for i, x1 in enumerate('#' + text1):
            for j, x2 in enumerate('#' + text2):
                if x1 == '#' or x2 == '#':
                    dp_map["%d-%d" % (i, j)] = 0
                elif x1 == x2:
                    dp_map["%d-%d" % (i, j)] = dp_map["%d-%d" % (i - 1, j - 1)] + 1
                else:
                    dp_map["%d-%d" % (i, j)] = max(dp_map["%d-%d" % (i - 1, j)], dp_map["%d-%d" % (i, j - 1)])
        return dp_map["%d-%d" % (len(text1), len(text2))]


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(3, s.longestCommonSubsequence(text1, text2))

    def test2(self):
        s = Solution()
        text1 = "abc"
        text2 = "abc"
        self.assertEqual(3, s.longestCommonSubsequence(text1, text2))

    def test3(self):
        s = Solution()
        text1 = "abc"
        text2 = "def"
        self.assertEqual(0, s.longestCommonSubsequence(text1, text2))

    def test4(self):
        s = Solution()
        text1 = "bsbininm"
        text2 = "jmjkbkjkv"
        self.assertEqual(1, s.longestCommonSubsequence(text1, text2))


if __name__ == '__main__':
    unittest.main()
