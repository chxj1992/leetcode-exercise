import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.exists = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TreeNode(c)
            root = root.children[c]
        root.exists = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.exists

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def backtrack(x: int, y: int, prefix: str):
            if 0 <= y < len(board) and 0 <= x < len(board[0]):
                if board[y][x] == '#':
                    return
                tmp = board[y][x]
                prefix += tmp
                board[y][x] = '#'
                if trie.search(prefix):
                    res.add(prefix)
                if trie.startsWith(prefix):
                    for (_x, _y) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        backtrack(x + _x, y + _y, prefix)
                board[y][x] = tmp

        res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(j, i, "")

        return list(res)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        words = ["oath", "pea", "eat", "rain"]
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        self.assertEqual(sorted(["eat", "oath"]), sorted(s.findWords(board, words)))


if __name__ == '__main__':
    unittest.main()
