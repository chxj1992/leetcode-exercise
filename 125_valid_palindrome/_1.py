import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        while s:
            if not s[0].isalnum():
                s = s[1:]
                continue
            if not s[-1].isalnum():
                s = s[:-1]
                continue
            if s[0].lower() != s[-1].lower():
                return False
            s = s[1:-1]
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(False, s.isPalindrome("race a car"))
        self.assertEqual(False, s.isPalindrome("0P"))


if __name__ == '__main__':
    unittest.main()
