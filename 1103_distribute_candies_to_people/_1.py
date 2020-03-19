import unittest
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        curr_candies, i, res = 1, 0, [0] * num_people
        while candies > curr_candies:
            res[i] += curr_candies
            i = (i + 1) % num_people
            candies -= curr_candies
            curr_candies += 1
        res[i] += candies
        return res


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual([1, 2, 3, 1], s.distributeCandies(7, 4))

    def test2(self):
        s = Solution()
        self.assertEqual([5, 2, 3], s.distributeCandies(10, 3))


if __name__ == '__main__':
    unittest.main()
