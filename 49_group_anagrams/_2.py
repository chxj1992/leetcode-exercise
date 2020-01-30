import unittest
from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n)
        Space: O(n)
        Timeout!
        """
        words_map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in words_map:
                words_map[key] = words_map[key] + [word]
            else:
                words_map[key] = [word]
        return list(words_map.values())


class Test(unittest.TestCase):

    def test1(self):
        """
        输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
        输出:
        [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]
        """
        s = Solution()
        actual = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
        self.assertEqual(len(expected), len(actual))
        for i, row in enumerate(expected):
            self.assertCountEqual(row, actual[i])

    def test2(self):
        s = Solution()
        actual = s.groupAnagrams(["", "", ""])
        expected = [
            ["", "", ""]
        ]
        self.assertEqual(len(expected), len(actual))
        for i, row in enumerate(expected):
            self.assertCountEqual(row, actual[i])


if __name__ == '__main__':
    unittest.main()
