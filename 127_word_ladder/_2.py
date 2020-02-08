import string
import unittest
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()
        step = 0
        queue = [beginWord]
        while queue:
            step += 1
            row = []
            for word in queue:
                for i, x in enumerate(word):
                    for c in string.ascii_lowercase:
                        change = word[:i] + c + word[i + 1:]
                        if change in visited or change not in wordSet:
                            continue
                        elif change == endWord:
                            return step + 1
                        else:
                            visited.add(change)
                            row.append(change)
            queue = row
        return 0


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

        self.assertEqual(5, s.ladderLength(beginWord, endWord, wordList))

    def test2(self):
        s = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]

        self.assertEqual(0, s.ladderLength(beginWord, endWord, wordList))


if __name__ == '__main__':
    unittest.main()
