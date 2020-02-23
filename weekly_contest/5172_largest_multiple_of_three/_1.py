import unittest
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digit_map = {}
        total = 0
        for digit in digits:
            total += digit
            digit_list = digit_map.setdefault(digit % 3, [])
            digit_list.append(digit)

        if total == 0:
            return '0'

        if total % 3 == 1:
            if 1 in digit_map:
                digit_map[1].remove(min(digit_map[1]))
            elif 2 in digit_map:
                digit_map[2].remove(min(digit_map[2]))
                digit_map[2].remove(min(digit_map[2]))
            else:
                return ''

        if total % 3 == 2:
            if 2 in digit_map:
                digit_map[2].remove(min(digit_map[2]))
            elif 1 in digit_map:
                digit_map[1].remove(min(digit_map[1]))
                digit_map[1].remove(min(digit_map[1]))
            else:
                return ''

        choose = []
        for i in range(3):
            digit_list = digit_map.setdefault(i, [])
            choose += digit_list

        choose.sort(reverse=True)

        return ''.join([str(c) for c in choose])


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual("981", s.largestMultipleOfThree([8, 1, 9]))

    def test2(self):
        s = Solution()
        self.assertEqual("8760", s.largestMultipleOfThree([8, 6, 7, 1, 0]))

    def test3(self):
        s = Solution()
        self.assertEqual("", s.largestMultipleOfThree([1]))

    def test4(self):
        s = Solution()
        self.assertEqual("0", s.largestMultipleOfThree([0, 0, 0, 0, 0, 0]))

    def test5(self):
        s = Solution()
        self.assertEqual("111", s.largestMultipleOfThree([1, 1, 1, 2]))

    def test6(self):
        s = Solution()
        self.assertEqual("2211", s.largestMultipleOfThree([2, 2, 1, 1, 1]))

    def test7(self):
        s = Solution()
        self.assertEqual("", s.largestMultipleOfThree([5, 8]))

    def test8(self):
        s = Solution()
        self.assertEqual("987766221", s.largestMultipleOfThree([7, 8, 7, 2, 1, 2, 6, 6, 9, 2]))

    def test9(self):
        s = Solution()
        self.assertEqual("966", s.largestMultipleOfThree([9, 8, 6, 8, 6]))


if __name__ == '__main__':
    unittest.main()
