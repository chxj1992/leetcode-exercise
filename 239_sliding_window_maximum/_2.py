import unittest
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        res = []
        dep = deque()
        for i, x in enumerate(nums):
            while len(dep) > 0 and x > nums[dep[-1]]:
                dep.pop()

            if len(dep) > 0 and i - dep[0] >= k:
                dep.popleft()

            dep.append(i)

            if i >= k - 1:
                res.append(nums[dep[0]])
        return res


class Test(unittest.TestCase):

    def test1(self):
        """
        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]
        """
        s = Solution()
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

    def test2(self):
        s = Solution()
        self.assertEqual([1, -1], s.maxSlidingWindow([1, -1], 1))


if __name__ == '__main__':
    unittest.main()
