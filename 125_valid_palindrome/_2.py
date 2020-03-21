import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [i.lower() for i in s if i.isalnum()]
        return arr == arr[::-1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(False, s.isPalindrome("race a car"))
        self.assertEqual(False, s.isPalindrome("0P"))


if __name__ == '__main__':
    unittest.main()
