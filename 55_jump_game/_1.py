import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Timeout!
        """
        cache = {}

        def recursion(index: int):
            if index in cache:
                return cache[index]
            if len(nums[index:]) == 1 or not nums[index:]:
                cache[index] = True
                return True
            num = nums[index]
            if num == 0:
                cache[index] = False
                return False
            for i in reversed(range(1, num + 1)):
                if recursion(index + i):
                    cache[index] = True
                    return True
            cache[index] = False
            return False

        return recursion(0)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
