import unittest


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.len = 0
        self.data = [-1] * k
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        if self.front is None:
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front + self.k - 1) % self.k
        self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        if self.rear is None:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
        self.data[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        if self.isEmpty():
            self.front = None
            self.rear = None
        else:
            self.front = (self.front + 1) % self.k
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        if self.isEmpty():
            self.front = None
            self.rear = None
        else:
            self.rear = (self.rear + self.k - 1) % self.k
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k


class Test(unittest.TestCase):

    def test1(self):
        deq = MyCircularDeque(3)
        self.assertEqual(True, deq.insertLast(1))
        self.assertEqual(True, deq.insertLast(2))
        self.assertEqual(True, deq.insertFront(3))
        self.assertEqual(False, deq.insertFront(4))
        self.assertEqual(2, deq.getRear())
        self.assertEqual(True, deq.isFull())
        self.assertEqual(True, deq.deleteLast())
        self.assertEqual(True, deq.insertFront(4))
        self.assertEqual(4, deq.getFront())

    def test2(self):
        deq = MyCircularDeque(8)
        self.assertEqual(True, deq.insertFront(5))
        self.assertEqual(5, deq.getFront())
        self.assertEqual(False, deq.isEmpty())
        self.assertEqual(True, deq.deleteFront())
        self.assertEqual(True, deq.insertLast(3))
        self.assertEqual(3, deq.getRear())
        self.assertEqual(True, deq.insertLast(7))
        self.assertEqual(True, deq.insertFront(7))
        self.assertEqual(True, deq.deleteLast())
        self.assertEqual(True, deq.insertLast(4))
        self.assertEqual(False, deq.isEmpty())

    def test3(self):
        deq = MyCircularDeque(5)
        self.assertEqual(True, deq.insertFront(7))
        self.assertEqual(True, deq.insertLast(0))
        self.assertEqual(7, deq.getFront())
        self.assertEqual(True, deq.insertLast(3))
        self.assertEqual(7, deq.getFront())
        self.assertEqual(True, deq.insertFront(9))
        self.assertEqual(3, deq.getRear())
        self.assertEqual(9, deq.getFront())
        self.assertEqual(9, deq.getFront())
        self.assertEqual(True, deq.deleteLast())
        self.assertEqual(0, deq.getRear())


if __name__ == '__main__':
    unittest.main()
