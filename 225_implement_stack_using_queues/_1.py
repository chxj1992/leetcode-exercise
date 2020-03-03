import unittest


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0


class Test(unittest.TestCase):

    def test(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(True, s.empty())


if __name__ == '__main__':
    unittest.main()
