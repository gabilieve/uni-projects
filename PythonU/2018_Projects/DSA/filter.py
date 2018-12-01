# import csv
from ll import *
import menu as mn
# import menu as menuboi
"""
ADTs used: Linked List from Practical 4
Reasoning:
Saving unique lists for comparison of user inputs and indexing of lists to allow for proper sorting algorithm
"""
class State:
    def __init__(self):
        ###PartyN was an attempt to essentially print a list of party names
        #With their appropriate abbreviations, but was not working
        fileobj = open("HouseCandidatesDownload-20499.csv","r") #Reading each line of file
        self.state = DSALinkedList() #List of states
        self.party = DSALinkedList() #Party abbreviations
        # self.partyN = list() #Names of parties
        self.div = DSALinkedList() #List of divisions
        self.result = DSALinkedList() #List of results
        self.lst = None #Sorting values
        self.pty = None #Set party to be none (needed for inserting elements into sorting list)
        self.divi = None #Set division to be none (needed for inserting elements into sorting list)
        self.loc = None
        self.lines = fileobj.readlines()
        for line in self.lines[2:]:
            self.row = line.split(",")
            if self.row[0] not in self.state: #If state not in list
                self.state.insertLast(self.row[0]) #Add to list
            elif self.row[3] not in self.party: #If party not in list
                self.party.insertLast(self.row[3]) #Add to list
            elif self.row[2] not in self.div: #If division not in list
                self.div.insertLast(self.row[2]) #Add to list
        self.Option1()

    def yeet(self):
        """Function used to check what user would like to do after exiting the first section"""
        userIn = str(input("\nWould you like to display the unsorted results? (Y/N) > ").upper())
        if userIn == "Y":
            self.showUResults()
        elif userIn == "N":
            userC = str(input("\nWould you like to sort the results? (Y/N) > ").upper())
            if userC == "Y":
                self.sortBy()
            elif userC == "N":
                user = str(input("Would you like to export the results as a CSV? (Y/N) > ").upper())
                if user == "Y":
                    self.CSVexp()
                elif user == "N":
                    print("\nThank you for playing Part 1")
                    mn.Menu()
                else:
                    print("Command not recognized, sending back to main menu")
                    mn.Menu()
            else:
                print("Command not recognized, sending back to main menu")
                mn.Menu()
        else:
            print("Command not recognized, sending back to main menu")
            mn.Menu()

    def showUResults(self): #Unsorted results
        """Function for showing unsorted results"""
        for val in self.result:
            print(val)
        userC = str(input("\nWould you like to sort the results? (Y/N) > ").upper())
        if userC == "Y":
            self.sortBy()
        elif userC == "N":
            userIn = str(input("Would you like to export the results as a CSV? (Y/N) > ").upper())
            if userIn == "Y":
                self.CSVexp()
            elif userIn == "N":
                men = str(input("Would you like to go back to the menu? (Y/N) > ").upper())
                if men == "Y":
                    print("\nThank you for playing")
                    mn.Menu()
                elif men == "N":
                    print("Restarting Part 1")
                    State()
                else:
                    print("Input not recognized, sending back to menu")
                    mn.Menu()
            else:
                print("Input not recognized, restarting Part 1")
                mn.Menu()
        else:
            print("\nInput not recognized, sending back to menu")
            mn.Menu()

    def sortBy(self):
        #Check the input of what the user would like to sort by
        user = str(input("What would you like to sort by? (Surname, State, Party or Division) > ").lower())
        if user == "surname": #If surname, return 6 (corresponding surname column)
            self.val = 6
        elif user == "state": #If state, return 0 (corresponding state column)
            self.val = 0
        elif user == "party": #If party, return 4 (corresponding full party name column)
            self.val = 4
        elif user == "division": #If division, return 2 (corresponding division column)
            self.val = 2
        self.bubbleSort(self.result) #Carry through to bubble sorting algorithm

    def bubbleSort(self, A):
        self.lst = A #Set result to be a new list to alter it without changing self.result
        sorted = False #set sorted to false
        while not sorted: #while sorted is false
            sorted = True #Assume its sorted
            for i in range(1, self.lst.length()): # for lists inside the length of the whole list
                for j in range(0, self.lst.length()-i): #for element inside length of lists, take i (each list once in correct place) - 1 (last list is limiting value)
                    if self.lst[j][self.val] > self.lst[j+1][self.val]: #If element in current list is greater than the next element
                        temp = self.lst[j] #temporarily set current list to a variable
                        self.lst[j] = self.lst[j+1] #make current element be the next element along
                        self.lst[j+1] = temp #set next element to be the value of temporary element
                        sorted = False #make sorted false once again to restart loop
        user = str(input("Would you like to display results? (Y/N) > ").upper()) #Check if user wants to display results
        self.ll = DSALinkedList()
        for i in self.lst:
            self.ll.insertLast(i)
        if user == "Y": #If yes
            self.showResult() #Passes it into results function
        elif user == "N": #If no
            user = str(input("Would you like to export the results as a csv file? (Y/N) > ").upper()) #Check if user wants to export it as a csv
            if user == "Y": #If yes
                self.CSVexp() #Pass through to CSV function
                # return self.lst
            elif user == "N": #If no
                print("Thank you for playing, sending back to main menu") #Exit or ask if they would like to restart
                mn.Menu()
            else:
                print("\nInput not recognized, sending back to menu")
                mn.Menu()

        return self.lst #Returns list to be used in sorting

    def showResult(self):
        """Function to show results"""
        for i in self.ll:
            print(i) #Print each element of list
        userIn = str(input("Would you like to export the results as a csv file? (Y/N) > ").upper())
        if userIn == "Y": #If user is yes
            self.CSVexp() #Pass through to CSV function
        elif userIn == "N": #If user is no
            print("Thank you for playing, sending back to main menu") #Exit or ask if they would like to restart
            mn.Menu()
        else:
            print("Thank you for playing, sending back to main menu") #Exit or ask if they would like to restart
            mn.Menu()

    def CSVexp(self):
        """Function to export file as CSV"""
        myfile = open("Part1.csv", 'w') #Opens file
        if self.lst is None: #Checks if it came from unsorted/sorted
            for line in self.result: #For each line
                for item in line: #For each value
                    myfile.write(item + ',') #Write it to a csv split by comma
                myfile.write('\n') #Newline for each line
        elif self.lst is not None:  #Checks if it came from unsorted/sorted
            for line in self.lst: #For each line
                for item in line: #For each value
                    myfile.write(item + ',') #write it to csv split by comma
                myfile.write('\n') #Newline for each line
        myfile.close() #Close so it cannot be changed
        print(f"""
        CSV file saved under name Part1.csv. Thank you for playing Part 1!
        Sending back to Main Menu""")
        mn.Menu()

    def notRecog(self):
        print("=============================================================================\n")
        print("command was not recognized sending back to start".upper())
        print("\n=============================================================================\n")
        State()

    def Option1(self):
        self.stateU = DSALinkedList() #User list of  input states
        self.partyU = DSALinkedList() #User list of input parties
        self.divU = DSALinkedList() #User list of input divisions
        # self.result = DSALinkedList()
        print("\n\nSelect what to filter by")
        print("""
        1. State
        2. Party
        3. Division
        """)
        user = str(input("Select filter > ").lower()) #Allow user to select their first filter choice
        if user == "state" or user == "1": #Start state search function
            return self.Option2(1)
        elif user == "party" or user == "2": #Start party search function
            return self.Option2(2)
        elif user == "division" or user == "3":
            return self.Option2(3) #Start division search function
        else:
            self.notRecog()
        # self.Option2()

    def Option2(self, value):
        print("=============================================================================")
        user = str(input("Would you like to sort by anything else? (Y/N) > ").upper())
        if value == 1:
            if user == "Y": #If user is yes
                print("=============================================================================\n")
                print("What other category would you like to filter by? (Party, Div) > ")
                user = str(input("\nSelect filter (Party, Div) > ").lower()) #Allow to select either party or division as 2nd option
                if user == "party": #If selection is party
                    user = str(input("\nWould you like to filter by Division as well? (Y/N) > ").upper()) #Check if user would like to filter by division
                    if user == "Y": #If input is yes
                        return self.statePartyDiv()
                    elif user == "N":
                        return self.stateParty()
                elif user == "div": #if Selection is division
                    user = str(input("\nWould you like to filter by Party as well? (Y/N) > ").upper()) #Check if user would like to filted by party
                    if user == "Y": #If input is yes
                        return self.stateDivParty() #Function to sort by state, division, party
                    elif user == "N": #If input is no
                        self.pty = None #Set party to be none (needed for inserting elements into sorting list)
                        return self.stateDiv() #Function to filter by state and division
                else:
                    self.notRecog()
            elif user == "N":
                return self.stateS()
            else:
                self.notRecog()

        elif value == 2:
            if user == "Y":
                print("=============================================================================\n")
                print("What other category would you like to filter by? (State, Div) > ")
                user = str(input("\nSelect filter (State, Div) ").lower()) #Allow to select either state or division as 2nd option
                if user == "state": #If selection is state
                    user = str(input("\nWould you like to filter by Division as well? (Y/N) > ").upper())  #Check if user would like to filter by division as well
                    if user == "Y":
                        return self.partyStateDiv()
                    elif user == "N":
                        return self.partyState()
                elif user == "div": #If selection is division
                    user = str(input("Would you like to filter by State as well? (Y/N) > ").upper()) #Check if user would like to filter by state as well
                    if user == "Y": #If user is yes
                        return self.partyDivState()  #Function to filter by party, division and state
                    elif user == "N": #If user is no
                        return self.partyDiv()
                else:
                    self.notRecog()

            elif user == "N":
                return self.partyS()

            else:
                self.notRecog()

        elif value == 3:
            if user == "Y":
                print("=============================================================================\n")
                print("What other category would you like to filter by? (State, Party) > ")
                user = str(input("\nSelect filter (State, Party) ").lower()) #Allow to select either state or party
                if user == "state": #If selection is state
                    user = str(input("\nWould you like to filter by Party as well? (Y/N) > ").upper()) #Check if user would like to filter by party as well
                    if user == "Y": #If user is yes
                        return self.divStateParty() #Function to filter by division, state and party
                    elif user == "N": #If user is no
                        self.pty = None #Set party to be none (needed for inserting elements into sorting list)
                        return self.divState() #Function to filter by division and state
                elif user == "party": #If selection is party
                    user = str(input("\nWould you like to filter by State as well? (Y/N) > ").upper()) #Check if user would like to filter by state as well
                    if user == "Y": #If user is yes
                        return self.divPartyState() #Function to filter by division, party and state
                    elif user == "N": #If user is no
                        self.loc = None #Set state to be none (needed for inserting elements into sorting list)
                        return self.divParty() #Function to filter by division and party
                else:
                    self.notRecog()
            elif user == "N":
                return self.divS()
            else:
                self.notRecog()

    def stateS(self): #State search (first selection was state)
        print("=============================================================================")
        amount = int(input("How many states would you like to display? > ")) #Select number of states to filter by
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counter = 0 #Start a counter at 0
        while counter != amount: #Compare counter amount to user input amount
            user = str(input(f"Select state number {(counter+1)} > ").upper()) #Select state #i+1 (since indexing starts at 0, add 1)
            self.stateU.insertLast(user) #Insert user input into linked list
            counter += 1 #Increase counter by 1 until it equals to the amount selected by user
        for line in self.lines[2:]:
            row = line.split(",")
            for self.loc in self.stateU: #For location in user selection of states
                if self.loc == row[0]: #If user state selection equals that of any state in the file
                    if row not in self.result:
                        self.result.insertLast(row[0:7])
        self.yeet()
        return self.result

    def partyS(self): #Party search (first selection was party)
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party) #Print each party abbreviation saved in original list
        print("=============================================================================")
        amount = int(input("How many parties would you like to display (Parties list displayed above)? > ")) #Select number of parties to filter by
        print(f"What party(ies) would you like to look at \n")
        counter = 0 #Start a counter
        while counter != amount: #Compare counter amount to user input amount
            user = str(input(f"Select party number {(counter+1)} > ").upper())  #Select party #i+1 (since indexing starts at 0, add 1)
            self.partyU.insertLast(user) #Insert user input into linked list
            counter += 1 #Increase counter by 1 until it equals to the amount selected by user
        for line in self.lines[2:]:
            row = line.split(",")
            for self.pty in self.partyU: #For party in user selection of parties
                if self.pty == row[3]:  #If user party selection equals that of any party in the file
                    if row not in self.result:
                        self.result.insertLast(row)
        self.yeet()
        return self.result

    def divS(self): #Division search (first selection was division)
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div) #Print each division from original list
        print("=============================================================================")
        amount = int(input("How many divisions would you like to display (Division list displayed above)? > ")) #Select number of divisions to filter by
        print(f"What division(s) would you like to look at \n")
        counter = 0 #Start a counter
        while counter != amount: #Compare counter to user amount
            user = str(input(f"Select division number #{(counter+1)} > ").title())  #Select division #i+1 (since indexing starts at 0, add 1)
            self.divU.insertLast(user) #Insert user input into linked list
            counter += 1 #Increase counter by 1 until it equals to amount selected by users
        for line in self.lines[2:]:
            row = line.split(",")
            for self.div in self.divU: #For division in user selection of divisions
                if self.div == row[2]:  #If user division selection equals that of any division in the file
                    if row not in self.result:
                        self.result.insertLast(row)
        self.yeet()

    def stateParty(self): #State and Party search
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both state and party must meet conditions to be processed through to sorting algorithm
        """
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        self.SP()
        self.yeet()


    def stateDiv(self):
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both state and division must meet conditions to be processed through to sorting algorithm
        """
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many divisions would you like to display (Division list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        self.SD()
        self.yeet()

    def partyState(self):
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both party and state must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        self.SP()
        self.yeet()

    def partyDiv(self):
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both party and division must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many divisions would you like to display (Division list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").upper())
            self.divU.insertLast(user)
            counterDiv += 1
        self.PD()
        self.yeet()

    def divState(self):
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both division and state must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many divisions would you like to display (Division list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").upper())
            self.divU.insertLast(user)
            counterDiv += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        self.SD()
        self.yeet()

    def divParty(self):
        """
        Follows same processes as before however doing it with 2 selection rather than one
        Both division and party must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Division list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").upper())
            self.divU.insertLast(user)
            counterDiv += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        self.PD()
        self.yeet()

    def SP(self): #State and Party
        """These are adaptations from the earlier sections"""
        for line in self.lines[2:]:
            row = line.split(",")
            for self.loc in self.stateU:
                if self.loc == row[0]:
                    for self.pty in self.partyU:
                        if self.pty == row[3]:
                            if row not in self.result:
                                self.result.insertLast(row)
        return self.result

    def SD(self): #State and Division
        """These are adaptations from the earlier sections"""
        for line in self.lines[2:]:
            row = line.split(",")
            for self.loc in self.stateU:
                if self.loc == row[0]:
                    for entry in self.divU:
                        if entry == row[2]:
                            if row not in self.result:
                                self.result.insertLast(row)
        return self.result

    def PD(self): #Party and Division
        """These are adaptations from the earlier sections"""
        for line in self.lines[2:]:
            row = line.split(",")
            for self.pty in self.partyU:
                if self.pty == row[3]:
                    for entry in self.divU:
                        if entry == row[2]:
                            if row not in self.result:
                                self.result.insertLast(row)
        return self.result


    def statePartyDiv(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Divisions list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        self.ALL()
        self.yeet()

    def stateDivParty(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Divisions list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        self.ALL()
        self.yeet()

    def partyStateDiv(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display? (Divisions list displayed above) > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        self.ALL()
        self.yeet()

    def partyDivState(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Divisions list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        self.ALL()
        self.yeet()

    def divStateParty(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Divisions list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").title())
            self.divU.insertLast(user)
            counterDiv += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        self.ALL()
        self.yeet()

    def divPartyState(self):
        """
        Follows same processes as before however doing it with 3 selections rather than one
        All fields must meet conditions to be processed through to sorting algorithm
        """
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        print("=============================================================================")
        amountDiv = int(input("How many division would you like to display (Divisions list displayed above)? > "))
        print("What Division(s) would you like to look at? > ")
        counterDiv = 0
        while counterDiv != amountDiv:
            user = str(input(f"Select division number {(counterDiv+1)} > ").upper())
            self.divU.insertLast(user)
            counterDiv += 1
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        print("=============================================================================")
        amountParty = int(input("How many parties would you like to display (Parties list displayed above)? > "))
        print("What Party(ies) would you like to look at? > ")
        counterParty = 0
        while counterParty != amountParty:
            user = str(input(f"Select party number {(counterParty+1)} > ").upper())
            self.partyU.insertLast(user)
            counterParty += 1
        print("=============================================================================")
        amountState = int(input("How many states would you like to display? > "))
        print("What state(s) would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA)")
        counterState = 0
        while counterState != amountState:
            user = str(input(f"Select state number {(counterState+1)} > ").upper())
            self.stateU.insertLast(user)
            counterState += 1
        self.ALL()
        self.yeet()

    def ALL(self): #All fields filtering by
        """This is adaptations from the earlier sections"""
        for line in self.lines[2:]:
            row = line.split(",")
            for self.pty in self.partyU:
                if self.pty == row[3]:
                    for entry in self.divU:
                        if entry == row[2]:
                            for self.loc in self.stateU:
                                if self.loc == row[0]:
                                    if row not in self.result:
                                        self.result.insertLast(row)
        return self.result
