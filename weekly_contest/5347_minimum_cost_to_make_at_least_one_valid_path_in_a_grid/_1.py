import unittest

# Definition for singly-linked list.
from typing import List


class Solution:

    def __init__(self) -> None:
        self.min_cost = 10000

    def minCost(self, grid: List[List[int]]) -> int:
        """
        Timeout!
        """
        steps = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0),
        }
        width = len(grid[0])
        height = len(grid)
        target = (height - 1, width - 1)

        def backtrack(curr: tuple, curr_cost: int):
            if curr == target:
                self.min_cost = min(curr_cost, self.min_cost)
                return

            if curr[0] < 0 or curr[0] >= height or curr[1] < 0 or curr[1] >= width or grid[curr[0]][curr[1]] == '#':
                return

            for k, step in steps.items():
                tmp = grid[curr[0]][curr[1]]
                grid[curr[0]][curr[1]] = '#'
                next_position = (curr[0] + step[0], curr[1] + step[1])
                if k != tmp:
                    backtrack(next_position, curr_cost + 1)
                else:
                    backtrack(next_position, curr_cost)
                grid[curr[0]][curr[1]] = tmp

        backtrack((0, 0), 0)
        return self.min_cost


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(3, s.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))

    def test2(self):
        s = Solution()
        self.assertEqual(0, s.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))

    def test3(self):
        s = Solution()
        self.assertEqual(1, s.minCost([[1, 2], [4, 3]]))

    def test4(self):
        s = Solution()
        self.assertEqual(3, s.minCost([[2, 2, 2], [2, 2, 2]]))

    def test5(self):
        s = Solution()
        self.assertEqual(0, s.minCost([[4]]))


if __name__ == '__main__':
    unittest.main()
