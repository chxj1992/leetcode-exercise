import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len, curr_len = 0, 0
        for i, c in enumerate(s):
            if c in char_map:
                prev_i = char_map[c]
                max_len = max(curr_len, max_len)
                curr_len = i - prev_i
                char_map = {k: v for k, v in char_map.items() if v > prev_i}
            else:
                curr_len += 1
            char_map[c] = i
        return max(max_len, curr_len)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    unittest.main()
