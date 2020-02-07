import unittest
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def changable(src: str, dest: str):
            change = 0
            for i, x in enumerate(src):
                if x != dest[i]:
                    change += 1
                if change > 1:
                    return False
            return change == 1

        curr = [start]
        step = 0
        visited = set(start)
        while curr:
            step += 1
            row = []
            while curr:
                src = curr.pop()
                if src in visited:
                    continue
                visited.add(src)
                for dest in bank:
                    if changable(src, dest):
                        if dest == end:
                            return step
                        else:
                            row.append(dest)
            curr += row
        return -1


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        self.assertEqual(1, s.minMutation(start, end, bank))

    def test2(self):
        s = Solution()
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        self.assertEqual(2, s.minMutation(start, end, bank))

    def test3(self):
        s = Solution()
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        self.assertEqual(3, s.minMutation(start, end, bank))

    def test4(self):
        s = Solution()
        start = "AAAAAAAA"
        end = "CCCCCCCC"
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]
        self.assertEqual(-1, s.minMutation(start, end, bank))


if __name__ == '__main__':
    unittest.main()
