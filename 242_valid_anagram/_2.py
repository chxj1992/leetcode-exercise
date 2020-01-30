import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


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
