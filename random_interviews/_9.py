import unittest
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        834. 树中距离之和
        https://leetcode-cn.com/problems/sum-of-distances-in-tree/
        Timeout !
        """
        route_map = {}
        for edge in edges:
            s1 = route_map.setdefault(edge[0], set())
            s2 = route_map.setdefault(edge[1], set())
            s1.add(edge[1])
            s2.add(edge[0])

        cache = {}

        def dist(x: int, y: int, curr: int, visited: set):
            if curr == y:
                cache['%d-%d' % (y, x)] = len(visited)
                cache['%d-%d' % (x, y)] = len(visited)
                return
            for t in route_map[curr] - visited - set([x]):
                cache['%d-%d' % (t, x)] = len(visited) + 1
                cache['%d-%d' % (x, t)] = len(visited) + 1
                dist(x, y, t, visited.union(set([t])))

        total_list = []
        for i in range(N):
            total = 0
            for j in range(N):
                key = '%d-%d' % (i, j)
                if key not in cache:
                    dist(i, j, i, set())
                total += cache[key]
            total_list.append(total)

        return total_list


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual([8, 12, 6, 10, 10, 10],
                         s.sumOfDistancesInTree(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))

        if __name__ == '__main__':
            unittest.main()
