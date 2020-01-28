import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        chars = list(s)
        stack = []
        for x in chars:
            if x in '([{':
                stack.append(x)
            elif len(stack) == 0 or x != pairs[stack[-1]]:
                return False
            else:
                stack.pop()
        return False if len(stack) else True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(True, s.isValid("()"))
        self.assertEqual(True, s.isValid("()[]{}"))
        self.assertEqual(False, s.isValid("([)]"))
        self.assertEqual(True, s.isValid("{[]}"))
        self.assertEqual(False, s.isValid("]"))


if __name__ == '__main__':
    unittest.main()
