import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(s.strip()):
            if i == ' ':
                break
            count += 1

        return count


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(5, s.lengthOfLastWord("Hello World "))


if __name__ == '__main__':
    unittest.main()
