import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(_i: int) -> str:
            res = get_char(_i)
            start, end = _i - 1, _i + 1
            while start >= 0 and end < l:
                start_char = get_char(start)
                end_char = get_char(end)
                if start_char != end_char:
                    break
                res = start_char + res + end_char
                start -= 1
                end += 1
            return res

        def get_char(_i: int) -> str:
            if _i % 2 == 0:
                return ""
            else:
                return s[_i // 2]

        longest = ''
        l = len(s) * 2 + 1
        for i in range(l):
            curr = expand(i)
            if len(curr) > len(longest):
                longest = curr
        return longest


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual("bab", s.longestPalindrome("babad"))
        self.assertEqual("bb", s.longestPalindrome("cbbd"))


if __name__ == '__main__':
    unittest.main()
