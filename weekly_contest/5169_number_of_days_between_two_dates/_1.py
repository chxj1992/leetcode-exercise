import time
import unittest


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        time1 = time.mktime(time.strptime(date1, '%Y-%m-%d'))
        time2 = time.mktime(time.strptime(date2, '%Y-%m-%d'))
        diff = int(abs(time1 - time2))
        return diff // 86400


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(1, s.daysBetweenDates("2019-06-29", "2019-06-30"))

    def test2(self):
        s = Solution()
        self.assertEqual(15, s.daysBetweenDates("2020-01-15", "2019-12-31"))


if __name__ == '__main__':
    unittest.main()
