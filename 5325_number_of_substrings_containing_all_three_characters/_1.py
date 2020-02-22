import unittest


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        index_map = {}
        for i, x in enumerate(s):
            index_list = index_map.setdefault(x, [])
            index_list.append(i)

        count = 0
        l = len(s)
        while index_map.setdefault('a', []) and index_map.setdefault('b', []) and index_map.setdefault('c', []):
            start_index, end_index = float('infinity'), 0
            start_char, end_char = '', ''
            for k, index_list in index_map.items():
                if index_list[0] < start_index:
                    start_index = index_list[0]
                    start_char = k
                if index_list[0] > end_index:
                    end_index = index_list[0]
                    end_char = k
            index_map[start_char].pop(0)
            count += l - end_index
        return count


class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(10, s.numberOfSubstrings("abcabc"))
        self.assertEqual(3, s.numberOfSubstrings("aaacb"))
        self.assertEqual(1, s.numberOfSubstrings("abc"))


if __name__ == '__main__':
    unittest.main()
