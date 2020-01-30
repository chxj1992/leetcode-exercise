import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.len = 0
        self.k = k
        self.none = ListNode(-1)
        self.front = self.none
        self.rear = self.none

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        node = ListNode(value)
        node.prev = self.none
        node.next = self.front
        self.front.prev = node
        self.front = node
        if self.len == 1:
            self.rear = node
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.len += 1
        node = ListNode(value)
        node.prev = self.rear
        node.next = self.none
        self.rear.next = node
        self.rear = node
        if self.len == 1:
            self.front = node
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        self.front = self.front.next
        self.front.prev = self.none
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.len -= 1
        self.rear = self.rear.prev
        self.rear.next = self.none
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.rear.val

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
