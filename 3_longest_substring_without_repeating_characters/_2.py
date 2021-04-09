import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, l, curr, longest = 0, 0, len(s), 0, 0
        char_set = set()
        while l > j >= i:
            if s[j] not in char_set:
                char_set.add(s[j])
                curr += 1
                longest = max(longest, curr)
                j += 1
            else:
                char_set.remove(s[i])
                curr -= 1
                i += 1

        return longest


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(1, s.lengthOfLongestSubstring(" "))


if __name__ == '__main__':
    unittest.main()
