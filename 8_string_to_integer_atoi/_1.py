import unittest


class Solution:
    def myAtoi(self, str: str) -> int:
        negative = False
        start = False
        num = 0
        for i in str:
            if i == ' ' and not start:
                continue
            elif i == '+' and not start:
                start = True
            elif i == '-' and not start:
                negative = True
                start = True
            elif i.isnumeric():
                start = True
                num = num * 10 + int(i)
                if abs(num) >= pow(2, 31):
                    if negative:
                        num = pow(2, 31)
                    else:
                        num = pow(2, 31) - 1
                    break
            else:
                break
        return -num if negative else num


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(42, s.myAtoi("42"))
        self.assertEqual(-42, s.myAtoi("   -42"))
        self.assertEqual(42, s.myAtoi("   +42"))
        self.assertEqual(4193, s.myAtoi("4193 with words"))
        self.assertEqual(0, s.myAtoi("words and 987"))
        self.assertEqual(0, s.myAtoi("   +0 123"))
        self.assertEqual(-2147483648, s.myAtoi("-91283472332"))


if __name__ == '__main__':
    unittest.main()
