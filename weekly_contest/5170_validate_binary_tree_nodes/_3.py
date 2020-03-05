import unittest
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        queue = [0]
        visited = set()
        while queue:
            next_level = []
            while queue:
                i = queue.pop()
                if i in visited:
                    return False
                visited.add(i)
                if leftChild[i] != -1:
                    next_level.append(leftChild[i])
                if rightChild[i] != -1:
                    next_level.append(rightChild[i])
            queue = next_level
        return len(visited) == n


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))

    def test2(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))

    def test3(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(2, [1, 0], [-1, -1]))

    def test4(self):
        s = Solution()
        self.assertEqual(False, s.validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))

    def test5(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(5, [4, -1, 3, -1, -1], [1, 2, -1, -1, -1]))

    def test6(self):
        s = Solution()
        self.assertEqual(True, s.validateBinaryTreeNodes(5, [1, 3, -1, -1, -1], [-1, 2, 4, -1, -1]))


if __name__ == '__main__':
    unittest.main()
