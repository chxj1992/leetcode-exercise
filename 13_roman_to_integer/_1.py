import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        l = len(s)
        for i, c in enumerate(s):
            x = char_map[c]
            if i < l - 1 and x < char_map[s[i + 1]]:
                res -= x
            else:
                res += x
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(3, s.romanToInt("III"))
        self.assertEqual(4, s.romanToInt("IV"))
        self.assertEqual(9, s.romanToInt("IX"))
        self.assertEqual(58, s.romanToInt("LVIII"))
        self.assertEqual(1994, s.romanToInt("MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
