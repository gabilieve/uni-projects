import numpy as np
from linkedList import *
# ll = DSALinkedList()

class ListIterator():
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        result = self.current.getValue()
        self.current = self.current.getNext()
        return result

class Error(Exception):
    pass

class StackOverflowError(Error):
    #Exception raise if stack is overfull
    def __init__(self, message):
        self.message = message

class StackUnderFlowError(Error):
    #Exception raised if stack is underfull
    def __init__(self, message):
        self.message = message

class DSAQueue():

    def __init__(self, capacity = 100):
        # self.capacity = capacity
        self.queue = DSALinkedList()
        #print(self.queue)
        # self.count = 0
        # self.dq = 0
        #self.index = len(self.queue)

    def __str__(self):
        return self.queue

    def __iter__(self):
        return ListIterator(self.queue.head)

    def __next__(self):
        self.index = self.next
        return self.index

    # def display(self):
    #     print(f"queue {len(self.queue)}")
    #
    # def getCount(self):
    #     return self.count
    #
    # def isEmpty(self):
    #     return self.count == 0
    #
    # def isFull(self):
    #     return self.count == self.capacity

    def enqueue(self, value):
        self.queue.insertLast(value)
        # value = ll.insertLast(value)
        # if self.isFull():
        #     raise StackOverflowError('Stack is full')
        # else:
        #     temp = self.count
        #     self.queue[temp] = value
        #     self.count += 1
        # print(f"{value} enqueued")
        # print(f"current queue{self.queue} enqueued")
        # return self.queue

    def dequeue(self):
        frontVal = self.queue.removeFirst()
        # if self.isEmpty():
        #     raise StackUnderFlowError("Stack is empty")
        # else:
        #     frontVal = ll.removeFirst()
        #     self.count -= 1
        #     self.dq += 1
        #     self.queue[:] = self.queue[1:] + self.queue[:1]
        #     #self.queue = np.delete(self.queue, 0, None)
        # print(f"{frontVal} dequeued")
        # #print(f"{self.value} counter for dequeue")
        # print(self.queue)
        # print(f"{self.count} counter for values")
        # print(f"{len(self.queue)} CURRENT LENGTH")
        # return frontVal
        return frontVal

    def peek(self):
        self.queue.peekFirst()
        # if self.isEmpty():
        #     raise StackUnderFlowError('Stack is empty')
        # else:
        #     front = ll.peekFirst()
        # print(f"{front} is front value")
        # return front
