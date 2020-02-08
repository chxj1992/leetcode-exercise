import unittest
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Timeout !
        """
        def changable(begin: str, end: str):
            if len(begin) != len(end):
                return False
            change = 0
            for i, x in enumerate(begin):
                if x != end[i]:
                    change += 1
                if change > 1:
                    return False
            return change == 1

        queue = [beginWord]
        visited = set()
        step = 0
        while queue:
            step += 1
            row = []
            for src in queue:
                for dest in wordList:
                    if dest in visited:
                        continue
                    if changable(src, dest):
                        if dest == endWord:
                            return step + 1
                        row.append(dest)
                        visited.add(dest)
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
