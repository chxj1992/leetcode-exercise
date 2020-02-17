import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return i


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(2, s.removeElement([3, 2, 2, 3], 3))
        self.assertEqual(5, s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


if __name__ == '__main__':
    unittest.main()
