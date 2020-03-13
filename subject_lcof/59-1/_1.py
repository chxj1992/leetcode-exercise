import unittest
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start, end = -k + 1, 0
        deque = []
        res = []
        while end < len(nums):
            while deque and nums[deque[-1]] < nums[end]:
                deque.pop()
            deque.append(end)
            if deque[0] <= end - k:
                deque.pop(0)
            if start >= 0:
                res.append(nums[deque[0]])
            start += 1
            end += 1
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
        self.assertEqual([7, 4], s.maxSlidingWindow([7, 2, 4], 2))


if __name__ == '__main__':
    unittest.main()
