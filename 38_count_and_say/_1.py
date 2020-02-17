import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        def say(s: str):
            num = s[0]
            count = 1
            res = ''
            for i in s[1:]:
                if i != num:
                    res += str(count) + num
                    num = i
                    count = 1
                else:
                    count += 1
            return res + str(count) + num

        prev = '1'
        for i in range(2, n + 1):
            prev = say(prev)
        return prev


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual("1211", s.countAndSay(4))
        self.assertEqual("111221", s.countAndSay(5))


if __name__ == '__main__':
    unittest.main()
