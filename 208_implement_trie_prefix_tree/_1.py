import unittest


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


class Test(unittest.TestCase):

    def test(self):
        trie = Trie()

        trie.insert("apple")
        self.assertEqual(True, trie.search("apple"))
        self.assertEqual(False, trie.search("app"))
        self.assertEqual(True, trie.startsWith("app"))
        trie.insert("app")
        self.assertEqual(True, trie.search("app"))


if __name__ == '__main__':
    unittest.main()
