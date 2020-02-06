import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) // 2
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 0
            v = hash_map[i]
            hash_map[i] = v + 1
            if v + 1 > l:
                return i


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.majorityElement([3, 2, 3]))
        self.assertEqual(2, s.majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
