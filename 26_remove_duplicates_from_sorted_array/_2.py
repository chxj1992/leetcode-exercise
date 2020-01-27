import unittest


class Solution:
    def removeDuplicates(self, nums):
        i = 1
        n = len(nums)
        while i < n:
            if nums[i - 1] == nums[i]:
                del nums[i]
                n -= 1
            else:
                i += 1
        return n


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
