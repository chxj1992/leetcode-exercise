import unittest
from typing import List

"""
找出整数数组中符合如下条件的所有元素：
 小于等于其前面的所有元素，大于等于后面所有元素
 示例：
 输入: [10 8 9 7 6 5 1 3 2]
 输出: [10 7 6 5] 
"""


class Solution:

    def solve(self, nums: List[int]) -> List[int]:
        min_num = nums[0]
        res = [min_num]
        for i in nums[1:]:
            if i < min_num:
                res.append(i)
                min_num = i
            while res and i > res[-1]:
                res.pop()
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([10, 7, 6, 5], s.solve([10, 8, 9, 7, 6, 5, 1, 3, 2]))
        self.assertEqual([3, 1], s.solve([5, 8, 10, 6, 3, 1]))


if __name__ == '__main__':
    unittest.main()
