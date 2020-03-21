import unittest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        for i in s:
            hash_map.setdefault(i, 0)
            hash_map[i] += 1
        res = 0
        odd_flag = 0
        for i, v in hash_map.items():
            if v % 2 == 0:
                res += v
            else:
                odd_flag = 1
                res += v - 1
        return res + odd_flag


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(7, s.longestPalindrome("abccccdd"))


if __name__ == '__main__':
    unittest.main()
