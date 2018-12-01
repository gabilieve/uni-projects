class DSAListNode():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        # self.next = None
        # self.prev = None
    #
    def __str__(self):
        return str(self.value)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext
        return self.next
        #print(self.next)

    def setPrev(self, prev):
        self.prev = prev
        return self.prev

    def getPrev(self):
        return self.prev
