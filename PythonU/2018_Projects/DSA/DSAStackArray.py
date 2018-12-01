import numpy as np
from linkedList import *

ll = DSALinkedList()

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

class DSAStack():

    def __init__(self, capacity = 100):
        # self.capacity = capacity
        self.stack = DSALinkedList()
        # print(self.stack)
        # self.count = 0
        # self.index = len(self.stack)

    def __iter__(self):
        return ListIterator(self.stack.head)

    def __next__(self):
        self.index = self.next
        return self.index

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     # if self.current is None:
    #     #     raise StopIteration()
    #     for i in self.stack:
    #         self.current +=1
    #     # self.current = self.current.getNext()
    #     return self.current

    # def __str__(self):
        # return str(self.value)

    def __str__(self):
        #return str(self.value)
        return str(self.stack)

    def display(self):
        self.stack.displayList()

    def getCount(self):
        print(f"{self.count} current count")
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def push(self, value):
        self.stack.insertLast(value)
        # self.value = ll.insertLast(value)
        # if self.isFull():
        #     raise StackOverflowError('Stack is full')
        # else:
        #     temp = self.count
        #     self.stack[temp] = value
        #     self.count += 1
        # print(f"{value} pushed")
        # print(f"current stack {self.stack}, pushed")
        # return self.value

    def pop(self):
        pop = self.stack.removeLast()
        print(f"{pop} popped")
        # if self.isEmpty():
        #     raise StackUnderFlowError("Stack is Empty")
        # else:
        #     topVal = ll.removeLast()
        #     # topVal = self.top()
        #     self.count -= 1
        #     #self.stack[:] = self.stack[1:] + self.stack[:1]
        # #self.stack = np.delete(self.stack, self.count, None)
        #     print(f"{topVal} popped")
        # print(f"current stack {self.stack}, popped")
        # return topVal

    def top(self):
        self.stack.peekLast()
        # topVal = -1
        # if self.isEmpty():
        #     raise StackUnderFlowError('Stack is empty')
        # else:
        #     topVal = ll.peekLast()
        #     # temp = self.count
        #     # topVal = self.stack[temp - 1]
        # print(f"{topVal} is top value")
        # return topVal
