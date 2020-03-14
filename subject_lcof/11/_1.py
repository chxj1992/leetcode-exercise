import unittest


class Solution:
    def minArray(self, numbers: [int]) -> int:
        start, end = 0, len(numbers) - 1
        while start < end:
            mid = (start + end) // 2
            if numbers[mid] > numbers[end]:
                start = mid + 1
            elif numbers[mid] < numbers[end]:
                end = mid
            else:
                end -= 1
        return numbers[start]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(1, s.minArray([3, 4, 5, 1, 2]))
        self.assertEqual(0, s.minArray([2, 2, 2, 0, 1]))
        self.assertEqual(1, s.minArray([1, 3, 5]))
        self.assertEqual(1, s.minArray([3, 1]))
        self.assertEqual(1, s.minArray([1, 3, 3]))


if __name__ == '__main__':
    unittest.main()
