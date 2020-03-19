import unittest


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


class Test(unittest.TestCase):

    def test(self):
        m = MinStack()
        m.push(-2)
        m.push(0)
        m.push(-3)
        self.assertEqual(-3, m.min())
        m.pop()
        self.assertEqual(0, m.top())
        self.assertEqual(-2, m.min())


if __name__ == '__main__':
    unittest.main()
