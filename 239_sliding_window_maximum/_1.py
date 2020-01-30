import unittest
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(nk)
        Space: O(n-k-1)
        """
        res = []
        window = []
        for x in nums:
            window.insert(0, x)
            if len(window) < k:
                continue
            res.append(max(window))
            window.pop()
        return res


class Test(unittest.TestCase):

    def test(self):
        """
        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]
        """
        s = Solution()
        self.assertEqual([3, 3, 5, 5, 6, 7], s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))


if __name__ == '__main__':
    unittest.main()
