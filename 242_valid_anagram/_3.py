import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for i, c in enumerate(s):
            char_map[c] = 1 if c not in char_map else char_map[c] + 1
            char_map[t[i]] = -1 if t[i] not in char_map else char_map[t[i]] - 1
            if char_map[c] == 0:
                del char_map[c]
            if t[i] in char_map and char_map[t[i]] == 0:
                del char_map[t[i]]
        return len(char_map) == 0


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
