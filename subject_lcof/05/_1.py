import unittest


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            res += '%20' if i == ' ' else i
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertIn("We%20are%20happy.", s.replaceSpace("We are happy."))


if __name__ == '__main__':
    unittest.main()
