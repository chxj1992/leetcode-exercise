import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        hl = len(haystack)
        nl = len(needle)
        for index, char in enumerate(haystack):
            if index + nl > hl:
                return -1
            if haystack[index: index + nl] == needle:
                return index
        return -1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(2, s.strStr("hello", "ll"))
        self.assertEqual(-1, s.strStr("aaaaa", "bba"))


if __name__ == '__main__':
    unittest.main()
