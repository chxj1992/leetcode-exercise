import unittest


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # python3.6+ 字典默认有序
        hash_map = {}
        for i in s:
            c = hash_map.setdefault(i, 0)
            hash_map[i] = c + 1
        for k, v in hash_map.items():
            if v == 1:
                return k
        return " "


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual("b", s.firstUniqChar("abaccdeff"))
        self.assertEqual(" ", s.firstUniqChar(""))


if __name__ == '__main__':
    unittest.main()
