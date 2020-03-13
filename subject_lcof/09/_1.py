import unittest


class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(value)

    def deleteHead(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        if not self.s2:
            return -1
        return self.s2.pop()


class Test(unittest.TestCase):

    def test(self):
        q = CQueue()
        self.assertEqual(-1, q.deleteHead())
        q.appendTail(5)
        q.appendTail(2)
        self.assertEqual(5, q.deleteHead())
        self.assertEqual(2, q.deleteHead())


if __name__ == '__main__':
    unittest.main()
