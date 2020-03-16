import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        l = len(nums)
        end = l - 1

        if l == 0:
            return 0

        def find(s: int, e: int):
            while 0 <= e < l and 0 <= s < l and nums[e] >= nums[s]:
                mid = s + (e - s) // 2
                if nums[mid] > target:
                    e = mid - 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    return mid
            return -1

        def expand(pos: int):
            count = 1
            before, after = pos - 1, pos + 1
            while (before >= 0 and nums[before] == target) or (after < l and nums[after] == target):
                if before >= 0 and nums[before] == target:
                    before -= 1
                    count += 1
                if after < l and nums[after] == target:
                    after += 1
                    count += 1
            return count

        position = find(start, end)
        if position == -1:
            return 0
        return expand(position)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(2, s.search([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual(0, s.search([5, 7, 7, 8, 8, 10], 6))
        self.assertEqual(1, s.search([1], 1))
        self.assertEqual(0, s.search([1], 0))
        self.assertEqual(1, s.search([1, 4], 4))


if __name__ == '__main__':
    unittest.main()
