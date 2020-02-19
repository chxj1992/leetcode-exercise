import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        while n != 1:
            if n in hash_map:
                return False
            hash_map[n] = True
            i = n
            n = 0
            while i > 0:
                n += (i % 10) ** 2
                i //= 10
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isHappy(19))


if __name__ == '__main__':
    unittest.main()
