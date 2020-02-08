import unittest
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        hash_map = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'ACT',
            'T': 'ACG',
        }
        curr = [start]
        step = 0
        bank = set(bank)
        visited = set(start)
        while curr:
            step += 1
            row = []
            while curr:
                one = curr.pop()
                for i, x in enumerate(one):
                    for t in hash_map[x]:
                        change = one[:i] + t + one[i + 1:]
                        if change not in bank:
                            continue
                        elif change not in visited:
                            row.append(change)
                            visited.add(change)
                        if change == end:
                            return step
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
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC",
                "CCCCCCCA"]
        self.assertEqual(-1, s.minMutation(start, end, bank))


if __name__ == '__main__':
    unittest.main()
