import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        deleted = 0
        dup = None
        total = len(nums)
        for i in range(total):
            if dup is None:
                dup = nums[i]
            elif nums[i - deleted] != dup:
                dup = nums[i - deleted]
            else:
                del nums[i - deleted]
                deleted += 1
        return total - deleted


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        nums = [1, 1, 2]
        self.assertEqual(2, s.removeDuplicates(nums))
        self.assertEqual(nums, [1, 2])

    def test2(self):
        s = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, s.removeDuplicates(nums))
        self.assertEqual([0, 1, 2, 3, 4], nums)


if __name__ == '__main__':
    unittest.main()
