import unittest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n^2)
        Space: O(1)
        Timeout!
        """
        res = []
        while len(strs) > 0:
            curr = strs.pop(0)
            row = [curr]
            i = 0
            while i < len(strs):
                if sorted(curr) == sorted(strs[i]):
                    row.append(strs[i])
                    strs.pop(i)
                    continue
                i += 1
            res.append(row)
        return res


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
