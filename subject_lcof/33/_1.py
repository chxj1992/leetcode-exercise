import unittest

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        point = len(postorder) - 1
        found = False
        for k, val in enumerate(postorder[:-1]):
            if not found and val > root:
                found = True
                point = k
            elif found and val < root:
                return False
        return self.verifyPostorder(postorder[:point]) and self.verifyPostorder(postorder[point:-1])


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(False, s.verifyPostorder([1, 6, 3, 2, 5]))
        self.assertEqual(True, s.verifyPostorder([1, 3, 2, 6, 5]))
        self.assertEqual(False, s.verifyPostorder([5, 2, -17, -11, 25, 76, 62, 98, 92, 61]))


if __name__ == '__main__':
    unittest.main()
