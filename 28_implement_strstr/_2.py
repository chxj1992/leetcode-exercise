import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        offset_table = {}
        for i, x in enumerate(reversed(needle)):
            if x not in offset_table:
                offset_table[x] = i
        nl = len(needle)
        hl = len(haystack)
        i = 0
        while i + nl <= hl:
            if haystack[i:i + nl] == needle:
                return i
            elif i + nl < hl and haystack[i + nl] in offset_table:
                c = haystack[i + nl]
                i += offset_table[c] + 1
            else:
                i += nl
        return -1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(2, s.strStr("hello", "ll"))
        self.assertEqual(-1, s.strStr("aaaaa", "bba"))
        self.assertEqual(0, s.strStr("a", "a"))


if __name__ == '__main__':
    unittest.main()
