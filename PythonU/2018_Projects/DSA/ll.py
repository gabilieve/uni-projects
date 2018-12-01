from listNode import *
import sys

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

class DSALinkedList():
    def __init__(self):
        self.head = None #sets head value to be none
        self.tail = None #sets tail value to be none
        self.count = 0

    def __iter__(self):
        return ListIterator(self.head)

    def __next__(self):
        self.index = self.next
        return self.index
        # while self.max is not None:
            # max = self.max.getNext()
        # if self.index is None:
            # raise ValueError("Iteration cannot occur")
        # else:
            # self.index += 1
            # self.index = self.getNext()
        # return self.index

    def __str__(self):
        x = [i for i in self]
        return str(x)

    def __setitem__(self, Ritem, value):
        index = 0
        lstCount = iter(self)
        found = False
        while index < self.count and found == False:
            if index == Ritem:
                found = True
                lstCount.current.setValue(value)
            else:
                index += 1
                next(lstCount)


    def __getitem__(self, Rindex):
        index = 0
        lstCount = iter(self)
        found = False
        while index < self.count and found == False:
            if index == Rindex:
                found == True
                return lstCount.current.value
            else:
                index += 1
                next(lstCount)

    def length(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.getNext()
        return count

    def __repr__(self):
        return str(self.head)

    def displayList(self):
        if self.isEmpty():
            print("[]")
        else:
            tidy = []
            currNd = self.head
            while currNd.getNext() != None:
                tidy.append(currNd.value)
                currNd = currNd.getNext()
            tidy.append(currNd.value)
        return tidy

    def isEmpty(self):
        return self.head == None #checking to see if head value is empty

    def insertFirst(self, newValue):
        #New node being passed through
        newNd = DSAListNode(newValue)
        self.count += 1

        print(f"{newNd} is current node")
        if self.isEmpty():
            #head
            self.head = newNd
            self.tail = newNd
            # print(f"{self.head} current head")
            # print(f"{self.tail} current tail")
        else:
            x = newNd.setNext(self.head)
            y = newNd.setPrev(None)
            # print(f"{x} is next node")
            # print(f"{y} is prev node")
            # print(f"{self.head} is current head")
            self.head = newNd
            # print(f"{self.tail} is tail")
            # print(f"{self.head} is head")


    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        self.count += 1
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
            # print(f"{self.head}")
            # print(f"{self.tail}")
            newNd.setPrev(None)
            newNd.setNext(None)
        else:
            z = newNd.setPrev(self.tail)
            currNd = self.tail
            self.tail = newNd
            # print(f"{z} is previous")
            # newNd.setPrev(self.tail)
            # while currNd.getNext() != None:
            #     currNd = currNd.getNext()
            x = currNd.setNext(newNd)
            nxt = newNd.setNext(None)
            # self.head.getNext()
            # u = tmp.setNext(newNd)
            # print(f"{x} is current")
            # print(f"{nxt} is next")
            # print(f"{self.head} is the head")
            # print(f"{self.tail} is the tail")
            #return newNd

    def peekFirst(self):
        if self.isEmpty():
            sys.exit()
        else:
            self.nodeValue = self.head.getValue()
            print(f"{self.nodeValue} is the first value")
        return self.nodeValue

    def peekLast(self):
        if self.isEmpty():
            sys.exit()
        else:
            currNd = self.head
            while currNd.getNext() is not None:
                currNd = currNd.getNext()
            self.nodeValue = currNd.getValue()
            print(f"{self.nodeValue} last value")
        return self.nodeValue

    def removeFirst(self):
        if self.isEmpty():
            sys.exit()
        else:
            self.count -= 1
            self.nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            print(f"{self.nodeValue} removed")
        return str(self.nodeValue)

    def removeLast(self):
        if self.isEmpty():
            sys.exit()
        elif self.head.getNext() == None:
            self.nodeValue = self.head.getValue()
            self.head = None
        else:
            self.count -= 1
            self.nodeValue = self.tail
            prevNd = self.nodeValue.getPrev()
            self.tail = prevNd
            prevNd.setNext(None)
            # self.nodeValue = prevNd.getValue()
            # print(f"{self.nodeValue} removed")
        return self.nodeValue

        #     self.prevNd = None
        #     currNd = self.head
        #     while currNd.getNext() is not None:
        #         self.prevNd = currNd
        #         self.tail = self.prevNd
        #         currNd = currNd.getNext()
        #         print(currNd)
        #     self.prevNd.setNext(None)
        #     self.nodeValue = currNd.getValue()
        #     print(f"{self.nodeValue} removed")
        # return self.nodeValue
