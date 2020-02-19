import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if map1.setdefault(s[i], t[i]) != t[i] or map2.setdefault(t[i], s[i]) != s[i]:
                return False
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isIsomorphic("egg", "add"))
        self.assertEqual(False, s.isIsomorphic("foo", "bar"))
        self.assertEqual(True, s.isIsomorphic("paper", "title"))
        self.assertEqual(False, s.isIsomorphic("ab", "aa"))


if __name__ == '__main__':
    unittest.main()
