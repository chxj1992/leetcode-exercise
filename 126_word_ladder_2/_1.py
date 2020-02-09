import unittest
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Timeout!
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

        def insert(_src: str, _dest: str, _trace_map, _level: int):
            r = False
            if _src not in _trace_map:
                return r
            if _dest not in _trace_map:
                _trace_map[_dest] = []
            for one in _trace_map[_src]:
                if len(one) != _level or _dest in one:
                    continue
                _trace_map[_dest].append(one + [_dest])
                r = True
            return r

        queue = [beginWord]
        trace_map = {beginWord: [[beginWord]]}
        finish = False
        level = 1
        visited = set()
        while queue:
            row = set([])
            for src in queue:
                for dest in wordList:
                    if dest in visited:
                        continue
                    if changable(src, dest):
                        if not insert(src, dest, trace_map, level):
                            continue
                        if dest == endWord:
                            finish = True
                        row.add(dest)
            if finish:
                return trace_map[endWord]
            for one in row:
                visited.add(one)
            queue = row
            level += 1
        return []


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

        self.assertEqual(sorted([
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"]
        ]), sorted(s.findLadders(beginWord, endWord, wordList)))

    def test2(self):
        s = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]

        self.assertEqual(sorted([]), sorted(s.findLadders(beginWord, endWord, wordList)))

    def test3(self):
        s = Solution()
        beginWord = "a"
        endWord = "c"
        wordList = ["a", "b", "c"]

        self.assertEqual(sorted([["a", "c"]]), sorted(s.findLadders(beginWord, endWord, wordList)))

    def test4(self):
        s = Solution()
        beginWord = "red"
        endWord = "tax"
        wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]

        self.assertEqual(
            sorted([["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]]),
            sorted(s.findLadders(beginWord, endWord, wordList)))


if __name__ == '__main__':
    unittest.main()
