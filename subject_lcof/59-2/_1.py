import unittest


class MaxQueue:

    def __init__(self):
        self.queue = []
        self.deque = []

    def max_value(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        v = self.queue.pop(0)
        if v == self.deque[0]:
            self.deque.pop(0)
        return v


class Test(unittest.TestCase):

    def test(self):
        m = MaxQueue()
        m.push_back(1)
        m.push_back(2)
        self.assertEqual(2, m.max_value())
        self.assertEqual(1, m.pop_front())
        self.assertEqual(2, m.max_value())


if __name__ == '__main__':
    unittest.main()
