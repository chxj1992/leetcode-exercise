import unittest
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        jack = []
        prev = None
        for i in nums:
            if i == 0:
                jack.append(i)
                continue
            if prev:
                if i == prev or i - prev - 1 > len(jack):
                    return False
                else:
                    jack = jack[i - prev - 1:]
            prev = i
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isStraight([1, 2, 3, 4, 5]))
        self.assertEqual(True, s.isStraight([0, 0, 1, 2, 5]))


if __name__ == '__main__':
    unittest.main()
