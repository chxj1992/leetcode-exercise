import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = self.build_map(s)
        map2 = self.build_map(t)
        return map1 == map2

    def build_map(self, s):
        char_map = {}
        for i in s:
            char_map[i] = char_map[i] + 1 if i in char_map else 1
        return char_map


class Test(unittest.TestCase):

    def test(self):
        """
        输入: s = "anagram", t = "nagaram"
        输出: True
        """
        s = Solution()
        self.assertTrue(s.isAnagram("anagram", "nagaram"))
        self.assertFalse(s.isAnagram("rat", "cat"))


if __name__ == '__main__':
    unittest.main()
