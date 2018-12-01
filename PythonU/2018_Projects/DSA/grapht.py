from linkedList import *
from listNode import *
from DSAStackArray import *
from DSAQueueArray import *

class DSAGraphVertex:
    def __init__(self, label): #weight):
        self.label = label
        # self.weight = weight
        self.links = DSALinkedList()
        self.edgeW = DSALinkedList()
        # self.visited = None
    #
    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return str(self.links)

    def getLabel(self):
        return self.label

    # def getValue(self):
    #     return self.value
    # def getNext(self):
    #     ...
    # def getWeight(self):
    #     return self.weight

    # def getAdjacent(self):
    #     ...
    #
    # def addEdge(self, vertex):
    #     ...
    #     # edgeList = edgeList + edge
    #     # adjList = adjList + vertex
    #
    # def setVisited(self):
    #     ...
    #
    # def clearVisited(self):
    #     ...
    #
    # def getVisit(self):
    #     ...
    #
    # def isSource(self):
    #     ...
    #
    # def isTarget(self):
    #     ...
    #
    # def toString(self):
    #     ...


class DSAGraph(DSAGraphVertex):
    # vtx = DSAGraphVertex()
    def __init__(self):
        self.vertex = DSALinkedList()
        # self.weight = DSALinkedList()

    def __str__(self):
        return str(self.vertex)

    def addVertex(self, label):
        self.vertex.insertLast(DSAGraphVertex(label))
        # self.vertex.insertLast(label)
        # self.vertex.insertLast(DSA)
        # print(label)
        # print(f"{x} is a vertex")

    def display(self):
        for i in self.vertex:
            print(i.getLabel() + " ")  #+ i.getWeight())

    def addEdge(self, v1, v2, weight = "5", dir = False):
        if dir == False:
            self.getVertex(str(v1)).links.insertLast(str(v2)) #.weights #.insertLast(str(weight))
            self.getVertex(str(v1)).edgeW.insertLast(str(weight))

            self.getVertex(str(v2)).links.insertLast(str(v1)) #.weights #.insertLast(str(weight))
            self.getVertex(str(v2)).edgeW.insertLast(str(weight))
        elif dir == True:
            self.getVertex(str(v1)).links.insertLast(str(v2))

    def getVertextCount(self):
        count = 0
        for i in self.vertex:
            count += 1
        return count

    def getEdgeCount(self):
        count = 0
        for i in self.vertex:
            for ii in i.links:
                count += 1
        return count

    #Works weirdly
    def getVertex(self, label):
        x = self.vertex.head #Gets head value of vertex
        z = x.getValue() #gets current head value
        while z.getLabel() != label and x.getNext() != None : #Checks that labels are matching and if there isn't any values afterwards
            x = x.getNext() #updates label to be the next
            z = x.getValue() #gets the value of the label and restarts loop
        #once labels match return value and create link
        return z

    def dispLinks(self):
        #Displays links individually
        ### Figure out how to display weights alongside it
        for i in self.vertex:
            # print(i.getLabel() + str(i.links) + str(i.edgeW))
            for ii in i.links:
                # print(i.getLabel() + ii + i.getWeight())
                print(i.getLabel() + " " + ii+ str(i.edgeW)) #+ i.getWeight())
        # return i.getLabel()+ii
                # for j in i.edgeW:
                    # print(i.getLabel() + " " + ii + " " + j)

    def getAdjacent(self, vertex):
        #Gets adgencent edges to vertex
        print(self.getVertex(vertex).links)
        return self.getVertex(vertex).links


    #Not working
    def isAdjacent(self, v1, v2):
        #Checks for adjacency
        # print(self.getVertex(v1).getVertex(links(v2)) == True)
        return self.getVertex(v1).links(v2) == True

    def displayList(self):
        #Creates an adjacency list
        for i in self.vertex:
            print(i.getLabel() + ": " + str(i.links))

    def displayMatrix(self):
        ...


    def DFS(self, start):
        self.new = self.vertex
        self.visited = DSALinkedList()
        self.tr = DSALinkedList()
        self.stack = DSAStack()
        self.stack.push(start)
        self.visited.insertLast(start)
        while self.stack is not DSALinkedList().isEmpty():
            for ii in self.vertex: # for value in vertex
                for i in self.stack:
                    for j in ii.links:
                        if str(ii) == str(i):
                            if str(ii.links.head) not in self.visited:
                                self.stack.push(str(ii.links.head))
                                self.visited.insertLast(str(ii.links.head))
                                print(self.visited)
                            # elif str(ii.links.head) in self.visited:
                            #     x = ii.links.head
                            #     x = str(x.getNext())
                            #     while x not in self.visited:
                            #         x = x.getNext()
                            #         self.visited.insertLast(str(x))

            self.stack.pop()

                            # if str(ii.links.head) not in self.visited and str(ii.links.head) not in self.stack:
                            #     self.visited.insertLast(str(ii.links.head))
                            #     self.stack.push(str(ii.links.head))
                            #     print(f"Visited: {self.visited}")
                            #     print(f"Stack: {self.stack}\n")
                            # elif str(ii.links.head) in self.visited:
                            #     while str(ii.links.head) not in self.visited:
                            #         x = ii.links.getNext()
                            #         self.visited.insertLast(x)



                                #Type Casting leading to issues here


                # for j in ii.links: #for value in links
                #     while j not in self.visited: #while link value is not in self.visited
                #         self.visited.insertLast(str(j)) #add value to visited
                #
                #         if j not in self.stack: #if link value is not in stack
                #             self.stack.push(j) #push value into stack
                #         print(self.visited)



                        # for value in self.stack:
                        #     if value in self.vertex:
                        #         print("yes")
                        #     elif value not in self.stack:
                        #         print("nah")
                        #     else:
                        #         print("problem")


            # for i in self.vertex:
            #     for ii in i.links:
            #         if ii not in self.stack or ii not in self.visited:
            #             self.visited.insertLast(ii)
            #             self.stack.push(ii)
            #             print(f"{self.visited} yeet")
            # self.stack.pop()



            # for i in self.vertex:
            #     for ii in i.links:
            #         if ii not in self.stack:
            #             for value in self.stack:
            #                 print(value)
            #                 if value in self.vertex:
            #                     print(value)
            # self.stack.pop()
                        # self.stack.push(ii)
                        # print(self.stack)
                        # for i in self.stack:
                        #     print(i.links)
                    # elif ii in self.stack:
                    #     hd = i.links.head
                    #     result = hd.getNext()
                    #     self.stack.push(result)
                        # self.tr.insertLast(ii[0])
                        # self.stack.push(ii[0])
                        # print(self.tr)
                        # return self.stack



            ###Best code so far?
            # for ii in self.vertex:
            #     for j in ii.links:
            #         while j not in self.visited:
            #             self.visited.insertLast(str(j))
            #             if j not in self.stack:
            #                 self.stack.push(j)
            #             print(self.visited)
            # self.stack.pop()




            # for i in self.vertex:
            #     for ii in i.links:
            #         while ii  not in self.visited:
            #             self.new.removeLast()
            #             self.tr.insertLast(str(i))
            #             self.tr.insertLast(str(ii))
            #             self.visited.insertLast(str(ii))
            #             self.stack.push(ii)
            #         # print(self.stac)
            #         # print(self.visited)
            #         self.stack.pop()
            #         print(self.stack)
            #         print(self.visited)


    def BFS(self, start):
        self.visited = DSALinkedList()
        # self.tr = DSALinkedList()
        self.queue = DSAQueue()
        self.queue.enqueue(start)
        self.visited.insertLast(start)
        while self.queue is not DSALinkedList().isEmpty():
            x = self.queue.dequeue()
            for ii in self.vertex:
                for j in ii.links:
                    if str(x) == str(ii):
                        while str(j) not in self.visited:
                            self.visited.insertLast(j)
                            print(f"Final graph through BFS: {self.visited}\n")
                            self.queue.enqueue(str(j))
        return 
                            # self.visited.insertLast(str(j))

                        # if str(x) in self.vertex:
                        #     self.queue.enqueue(x.links)
                        # elif x not in self.vertex:
                        #     print("Something went wrong")
                        # else:
                        #     print("I have no idea what wrong")

                        #Dequeues values
                        # if j not in self.queue:
                        #     self.queue.enqueue(j)

            # for i in self.vertex:
            #     self.new.insertLast(str(i.links))
            #     print(self.new)
            #     self.visited.insertLast(str(i.links.head))
            #     self.stac.push(i.links.head)
            #     i.links.removeFirst()
            #     # print(self.stac)
            #     # print(self.visited)
            # self.stac.pop()
            # print(self.visited)

                # while i != self.vertex:
                #     self.new = str(i.links)
                #     print(self.new)
                #     # print()
                #     self.visited = i.getLabel()
                #     print(self.visited)
                #     # print()
                #     # i.links.removeLast()
                #     self.stac.push(self.new)
                # self.stac.pop()




            # while self.vertex in DSAGraphVertex(start).links:
            #     self.new = i.getLabel()+str(i.links)
            #     print(self.new)
            #     # print()
            #     self.old = i.getLabel()
            #     print(self.old)
            #     # print()
            #     # i.links.removeLast()
            #     self.stac.push(self.old)
            # self.stac.pop()





# class DSAGraphEdge(DSAGraphVertex):
#     def __init__(self, weight):
#         self.val = weight
#         self.weight = DSALinkedList()
#
#     # def __init__(self, label, value, source, target):
#     #     self.label = label
#     #     self.value = value
#     #     self.source = source
#     #     self.target = target
#     #     self.visited = None
#         # self.
#     def getWeight(self):
#         return self.val
#
#     def getLabel(self):
#         ...
#
#     def getValue(self):
#         ...
#
#     def getFrom(self):
#         ...
#
#     def getTo(self):
#         ...
#
#     def isDirected(self):
#         ...
#
#     def toString(self):
#         ...
