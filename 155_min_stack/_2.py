import unittest


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ordered = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.ordered) == 0 or x <= self.ordered[-1]:
            self.ordered.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.ordered[-1]:
            self.ordered.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class Test(unittest.TestCase):

    def test(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        minStack.top()
        self.assertEqual(0, minStack.top())
        self.assertEqual(-2, minStack.getMin())


if __name__ == '__main__':
    unittest.main()
