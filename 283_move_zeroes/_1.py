import unittest
from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Time: O(n)
        Space: O(1)
        """
        i = 0
        current_index = 0
        while i < len(nums):
            if nums[current_index] == 0:
                nums.append(nums.pop(current_index))
            else:
                current_index += 1
            i += 1


class TestStringMethods(unittest.TestCase):

    def test(self):
        """
        输入: [0,1,0,3,12]
        输出: [1,3,12,0,0]
        """
        s = Solution()
        l = [0, 1, 0, 3, 12]
        s.moveZeroes(l)
        self.assertEqual(l, [1, 3, 12, 0, 0])

    def test_2(self):
        """
        输入: [0,0,1]
        输出: [1,0,0]
        """
        s = Solution()
        l = [0, 0, 1]
        s.moveZeroes(l)
        self.assertEqual(l, [1, 0, 0])


if __name__ == '__main__':
    unittest.main()
