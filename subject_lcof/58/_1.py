import unittest


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual("cdefgab", s.reverseLeftWords("abcdefg", 2))
        self.assertEqual("umghlrlose", s.reverseLeftWords("lrloseumgh", 6))


if __name__ == '__main__':
    unittest.main()
