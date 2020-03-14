import unittest


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()

        def _sum(i: int):
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            return s

        def dfs(x: int, y: int):
            if x < m and y < n and _sum(x) + _sum(y) <= k:
                position = "%d-%d" % (x, y)
                if position in visited:
                    return
                visited.add(position)
                dfs(x + 1, y)
                dfs(x, y + 1)

        dfs(0, 0)
        return len(visited)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(3, s.movingCount(2, 3, 1))
        self.assertEqual(1, s.movingCount(3, 1, 0))
        self.assertEqual(88, s.movingCount(11, 8, 16))


if __name__ == '__main__':
    unittest.main()
