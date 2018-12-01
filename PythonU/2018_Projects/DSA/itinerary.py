from grapht import *
# from menu import *
import menu as mn

"""
ADTs used: Graphs, Queues, Linked Lists from Pracs 6 and 4 respectively
Reasoning:
Graphs are relatively easy to implement to allow for each location to be a vertex and link them together accordingly
Queues are used within Graphs for BFS traversal
Linked Lists are used to store all locations for comparison of edges and a unique location list. They are also found within Queues code.
"""

class Iti():
    def __init__(self):
        self.grp = DSAGraph() #Initiate Graph class
        # loadpath = "C:/Users/Gabriel/Desktop/University/2ndYear/Semester2/COMP1002/Assignment" #Sets the loadpath
        # self.path = loadpath + "/ElectDist1.0.csv" #Loads in electorate distance
        # self.division = loadpath + "/iti2.csv" #Loads in Part 3 itinerary
        # self.airport = loadpath + "/AirportDist1.0.csv" #Loads in airports distance
        self.start()

    def start(self):
        self.location = DSALinkedList() #Initiates a location list
        self.list = DSALinkedList()
        division = open("Part3.csv", 'r') #Opens Part 3 file
        airports = open("AirportDist1.0.csv", 'r') #Opens airport file
        longl = open("ElectDist1.0.csv" , 'r') #Opens electorate file
        self.ldiv = division.readlines()
        self.lair = airports.readlines()
        self.longl = longl.readlines()

        for row in self.ldiv[0:]: #for line in Part 3 file
            line = row.rstrip('\n').split(",") #Splits each line and strips newline character
            self.grp.addVertex(line[1]) #Create a vertex based on location
            self.location.insertLast(line[1]) #Insert location into a list


        #This had to be done for both to and from due to for some reason the fields not having the same name (this causes slight repetition)
        for row in self.lair[1:]: #For value in airport distance file
            destination = row.rstrip('\n').split(",") #Splits each line and strips newline character
            if destination[1] not in self.location: #If from location not in list
                self.location.insertLast(destination[1]) #Insert location into list
                self.grp.addVertex(destination[1]) #Create vertex of location (airport)
            elif destination[5] not in self.location: #If to location not in list
                self.location.insertLast(destination[5]) #Insert location into list
                self.grp.addVertex(destination[5]) #Create vertex of location (airport)
            self.grp.addEdge(destination[1], destination[5]) #Create an edge between each airport

        for item in self.longl[1:]: #For value in electorate distance
            check = item.rstrip('\n').split(",") #Splits each line and strips newline character
            if check[1] in self.location: #If from destination is in the location list
                if check[5] in self.location: #If to destination is in the location list
                    self.grp.addEdge(check[1], check[5]) #Create an edge between divisions

        self.edge()

    def edge(self):
        user = str(input("Would you like to display edges? (Y/N) > ").upper())
        if user == "Y":
            self.grp.displayList() #Displays edges
            print("\n\nNOTE: THIS PART DOES NOT CALCULATE MINIMUM DISTANCE IT JUST DISPLAYS RESULTS IN BFS FORMAT")
            print("AND UNFORTUNATELY DOES NOT RETURN TO MENU OR OFFER ANY OTHER OTPIONS")
            print("YOU HAVE BEEN WARNED\n")
            userC = str(input("Would you like to display the shortest path? (Y/N) > ").upper())
            if userC == "Y":
                self.breadth()
            elif userC == "N":
                print("\nReturning to main menu")
                mn.Menu()
        elif user == "N":
            print("\n\nNOTE: THIS PART DOES NOT CALCULATE MINIMUM DISTANCE IT JUST DISPLAYS RESULTS IN BFS FORMAT")
            print("AND UNFORTUNATELY DOES NOT RETURN TO MENU OR OFFER ANY OTHER OTPIONS")
            print("YOU HAVE BEEN WARNED\n")
            userC = str(input("Would you like to display the shortest path? (Y/N) > ").upper())
            if userC == "Y":
                self.breadth()
            elif userC == "N":
                men = str(input("Would you like to return to the main menu? (Y/N) > ").upper())
                if men == "Y":
                    print("\nReturning to main menu")
                    mn.Menu()
                elif men == "N":
                    print("Thank you for playing!")
                else:
                    self.exit(1)
        else:
            self.exit(1)

    def breadth(self):
        for val in self.grp.vertex:
            for i in val.links:
                if i not in self.list:
                    self.list.insertLast(i)
        # for i in self.grp.vertex: #For each vertex in the vertices list
        print("==========================================")
        print("These are the available starting location")
        print("==========================================")
        print(self.list)
        userLoc = str(input("Select starting location > ").title())
        # for i in self.grp.vertex: #For each vertex in the vertices list
        if userLoc in self.list: #Check is the user input is in the list of links
            self.grp.BFS(userLoc) #If it is proceed to do BFS with that division as the start
            print("yeet")
            return self.exit(3)
        elif userLoc not in self.list: #If it's not pass to exit
            return self.exit(2)
        else: #If input not recognized pass to exit
            return self.exit(1)


    def exit(self, value):
        """General exit function based on where the error occured of what point they have reached of the program"""
        if value == 1:
            print("Command not recognized")
            user = str(input("Would you like to quit back to menu? (Y/N) > ").upper())
            if user == "Y":
                print("Thank you for playing, going back to menu")
                mn.Menu()
            elif user == "N":
                userC = str(input("Would you like to restart part 4? (Y/N) > ").upper())
                if userC == "Y":
                    print("restarting part 4".upper())
                    Iti()
                elif userC == "N":
                    print("Thank you for playing part 4, sending back to main menu")
                    mn.Menu()
                else:
                    print("command not recognized, sending back to main menu".upper())
                    mn.Menu()
            else:
                print("command not recognized, sending back to main menu".upper())
                mn.Menu()
        elif value == 2:
            print("Location not found in list")
            user = str(input("Would you like to quit back to menu? (Y/N) > ").upper())
            if user == "Y":
                print("Thank you for playing, going back to menu")
                mn.Menu()
            elif user == "N":
                userC = str(input("Would you like to restart part 4? (Y/N) > ").upper())
                if userC == "Y":
                    print("restarting part 4").upper()
                    Iti()
                elif userC == "N":
                    print("Thank you for playing part 4, sending back to main menu")
                    mn.Menu()
                else:
                    print("command not recognized, sending back to main menu".upper())
                    mn.Menu()
            else:
                print("command not recognized, sending back to main menu".upper())
                mn.Menu()
        elif value == 3:
            # print("Thank you for playing")
            userC = str(input("Would you like to return to the main menu? (Y/N) > "))
            if userC == "Y":
                mn.Menu()
            elif userC == "N":
                print("Thank you for playing Candidate Selection 2016!")
                print("Note: We still know we are late on this")
            else:
                self.exit(1)


# it = Iti()
# it.start()
