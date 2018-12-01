from ll import *
# import csv
import menu as mn
"""
ADTs used: Linked List from Practical 4
Reasoning:
Saving unique lists for comparison of user inputs
"""

class Sub():
    def __init__(self):
        self.candidate = DSALinkedList() #List holding candidate names
        self.state = DSALinkedList() #List holding state names
        self.party = DSALinkedList() #List holding party names
        self.result = DSALinkedList()
        fileobj = open("HouseCandidatesDownload-20499.csv","r")
        self.lines = fileobj.readlines()
        for line in self.lines[2:]:
            row = line.split(",")
            if row[6].upper() not in self.candidate: #For every unique name
                self.candidate.insertLast(row[6].upper()) #Inser into candidate names list
            elif row[0] not in self.state: #For every unique state name
                self.state.insertLast(row[0]) #Insert into state names list
            elif row[3] not in self.party: #For every unique party name
                self.party.insertLast(row[3]) #Inser into party name list
        self.candSearch()

    def candSearch(self): #Start of candidate search
        print(f"What is the character of the surname of the candidate you would like to search by?")
        self.char = str(input("Select substring > ").upper()) #String of character to search for
        user = str(input("Would you like to filter by anything else? (Y/N) > ").upper()) #check if user wants to filter by more than substring
        if user == "Y": #If they do
            user = str(input("Would you like to filter by State or Party? > ").lower()) #Check whethere they want state or party
            if user == "state": #If state
                user = str(input('Would you like to filter by party as well? (Y/N) > ').upper()) #Ask if they want party as well
                if user  == "Y":
                    self.candStateParty() #Function to filter by everything
                elif user == "N":
                    self.candState() #Function to filter by substring and state

            elif user == "party": #If party
                user = str(input('Would you like to filter by state as well? (Y/N) > ').upper()) #Ask if they want State as well
                if user  == "Y":
                    self.candPartyState() #Function to filter by everything
                elif user == "N":
                    self.candParty() #Function to filter by substring and party

        elif user == "N":
            #Following same format as 'substring' function
            for line in self.lines[2:]:
                row = line.split(",")
                if str(row[6].upper()).find(self.char, 0) == 0: #If the substring entered matches that of any surnames beginning at index 0
                    self.result.insertLast(row)
        else:
            print("\n=============================================================================")
            print("Command not recgonized, returning to menu".upper())
            mn.Menu()
        self.showR()
        return self.result

    def candStateParty(self):
        userS = str(input("What state would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA) > ").upper()) #Allow user to select state
        for state in self.state:
            if userS == str(state): #compare user input to unique state list
                partyC = str(input(f"What party would you like to look at?\n {self.party} > ").upper()) #Allow user to select party
                print("\n==============================================")
                print("CANDIDATE RESULTS FROM CHOSEN CATEGORIES\n")
                for party in self.party:
                    if partyC == str(party): #Compare user input to unique party list
                    #Following same format as 'substring' function
                        for line in self.lines[2:]:
                            row = line.split(",")
                            if str(row[6].upper()).find(self.char, 0) == 0 and str(row[0]) == userS and str(row[3]) == partyC: #If all fields entered match those of any row on data
                                self.result.insertLast(row)
        self.showR()
        return self.result

    def candState(self):
        userS = str(input("What state would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA) > ").upper()) #Allow user to select state
        for state in self.state:
            if userS == str(state): #Compare user input to unique state list
                #Following same format as 'substring' function
                for line in self.lines[2:]:
                    row = line.split(",")
                    if str(row[6].upper()).find(self.char, 0) == 0 and str(row[0]) == userS: #If substring matches and state matches to state list
                        self.result.insertLast(row)
        self.showR()
        return self.result

    def candPartyState(self):
        partyC = str(input(f"What party would you like to look at?\n {self.party} > ").upper()) #Allow user to select party
        for party in self.party:
            if partyC == str(party): #Compare user input to list of parties
                userS = str(input("What state would you like to look at (ACT, NSW, NT, QLD, SA, TAS, VIC, WA) > ").upper()) #Allow user to select state
                for state in self.state:
                    if userS == str(state): #Compare user input to list of states
                        print("\n==============================================")
                        print("CANDIDATE RESULTS FROM CHOSEN CATEGORIES\n")
                        #Following same format as 'substring' function
                        for line in self.lines[2:]:
                            row = line.split(",")
                            if str(row[6].upper()).find(self.char, 0) == 0 and str(row[0]) == userS and str(row[3]) == partyC: #If all fields match
                                self.result.insertLast(row)
        self.showR()
        return self.result

    def candParty(self):
        partyC = str(input(f"What party would you like to look at?\n {self.party} > ").upper()) #Allow user to select party
        for party in self.party:
            if partyC == str(party): #Compare user input to list of parties
                print("\n==============================================")
                print("CANDIDATE RESULTS FROM CHOSEN CATEGORIES\n")
                #Following same format as 'substring' function
                for line in self.lines[2:]:
                    row = line.split(",")
                    if str(row[6].upper()).find(self.char, 0) == 0 and str(row[3]) == partyC: #If substring matches and party matches party list
                        self.result.insertLast(row)
        self.showR()
        return self.result

    def showR(self):
        """Function to check result and see what the user would like to do"""
        user = str(input("Would you like to display results? (Y/N) > ").upper())
        if user == "Y":
            for val in self.result:
                print(val)
            usercsv = str(input("Would you like to export the results as a CSV? (Y/N) > ").upper())
            if usercsv == "Y":
                self.CSVexp()
            elif usercsv == "N":
                userC = str(input("Would you like to return to the main menu? (Y/N) > ").upper())
                if userC == "Y":
                    print("\n=============================================================================")
                    print("Returning to main menu".upper())
                    mn.Menu()
                elif userC == "N":
                    print("Thank you for playing!")
                else:
                    print("\n=============================================================================")
                    print("Command not recognized, returning to menu")
                    mn.Menu()
        elif user == "N":
            usercsv = str(input("Would you like to export the results as a CSV? (Y/N) > ").upper())
            if usercsv == "Y":
                self.CSVexp()
            elif usercsv == "N":
                userC = str(input("Would you like to return to the main menu? (Y/N) > ").upper())
                if userC == "Y":
                    print("\n=============================================================================")
                    print("Returning to main menu".upper())
                    mn.Menu()
                elif userC == "N":
                    print("Thank you for playing!")
                else:
                    print("\n=============================================================================")
                    print("Command not recognized, returning to menu".upper())
                    mn.Menu()
            else:
                print("\n=============================================================================")
                print("Command not recognized, returning to menu".upper())
                mn.Menu()
        else:
            print("\n=============================================================================")
            print("Command not recgonized, returning to menu".upper())
            mn.Menu()

    def CSVexp(self):
        """Function to export file as a csv"""
        myfile = open("Part2.csv", "w") #Open file as a CSV
        for line in self.result: #For line in results
            for item in line: #For item in lines
                myfile.write(item + ',') #Write item seperated by a comma
            myfile.write('\n') #Add a newline after every line
        myfile.close() #Close file
        print(f"""
        CSV file saved under name Part2.csv. Thank you for playing Part 2!
        Sending back to Main Menu""")
        mn.Menu()


# https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
# https://docs.python.org/2.7/library/string.html#string.find Find method for substring
