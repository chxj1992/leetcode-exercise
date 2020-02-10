import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Timeout
        """
        cache = {}

        def recursion(index: int) -> int:
            if index in cache:
                return cache[index]
            if len(nums[index:]) == 1 or not nums[index:]:
                return 0
            num = nums[index]
            for i in reversed(range(1, num + 1)):
                sub = recursion(index + i)
                if sub >= 0:
                    cache[index] = min(cache[index], sub + 1) if index in cache else sub + 1
            return cache[index] if index in cache else -1

        return recursion(0)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, s.jump([2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
