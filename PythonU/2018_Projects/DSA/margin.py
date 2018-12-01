from linkedList import *
import csv
import os.path
import menu as mn

"""
ADTs used: Linked List from Practical 4
Reasoning:
Saving unique lists for comparison of user inputs
"""

class Margin():
    def __init__(self):
        if os.path.isfile("margin.csv"):
            fileobj = open("test.csv","r")
            self.lines= fileobj.readlines()

        else:
            fout=open("margin.csv","a")
            f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-ACT.csv")
            next(f)
            next(f)
            for line in f:
                fout.write(line)
            f.close()

            for num in range(2,9):
                if num == 2:
                    nsw = "NSW"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+nsw+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 3:
                    nt = "NT"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+nt+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 4:
                    qld = "QLD"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+qld+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 5:
                    sa = "SA"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+sa+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 6:
                    tas = "TAS"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+tas+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 7:
                    vic = "VIC"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+vic+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()

                if num == 8:
                    wa = "WA"
                    f = open("HouseStateFirstPrefsByPollingPlaceDownload-20499-"+wa+".csv")
                    next(f)
                    next(f)
                    for line in f:
                         fout.write(line)
                    f.close()
                    fout.close()

            fileobj = open("test.csv","r")
            self.lines = fileobj.readlines()
        self.splitting()

    def splitting(self):
        self.state = DSALinkedList() #Unique State list
        self.party = DSALinkedList() #Unique Party list
        self.div = DSALinkedList() #Unique division list
        self.result = DSALinkedList() #List to store results
        for line in self.lines[0:]:
            row = line.split(",")
            if row[11] not in self.party: #If party not in list
                self.party.insertLast(row[11]) #Insert party into list
            elif row[0] not in self.state: #If state not in list
                self.state.insertLast(row[0]) #Insert state into list
            elif row[2] not in self.div: #If division not in list
                self.div.insertLast(row[2]) #Insert division into list
        self.marginVote()

    def marginVote(self, margin = 6):
        self.userVal = None #Sets user margin input to None
        self.default = float(margin) #Sets margin to 6%
        self.party2Val = DSALinkedList() #Stores all votes for second party choice
        self.party2S = 0 #Sum of second party choice
        self.partyVal = DSALinkedList() #Stores all votes for first party choice
        self.partyS = 0 #Sum of first party choice
        self.otherVal = DSALinkedList() #If not second party, stores votes for all other parties
        self.otherS = 0 #Sum votes of all other parties
        self.divVal = DSALinkedList() #Stores votes in division
        self.divS = 0 #Sum of division votes
        user = str(input("Would you like to change the margin value from the default 6%? (Y/N) > ").upper())
        if user == "Y":
            self.userVal = float(input("Select margin to use > "))
            userIn = str(input("Would you like to select a division? (Y/N) > ").upper())
            if userIn == "Y":
                self.divChoice()
            elif userIn == "N":
                self.partyC()
            else:
                self.exit(1)
        elif user == "N":
            userIn = str(input("Would you like to select a division? (Y/N) > ").upper())
            if userIn == "Y":
                self.divChoice()
            elif userIn == "N":
                self.partyC()
            else:
                self.exit(1)
        else:
            self.exit(1)


    def divChoice(self):
        print("\n=============================================================================")
        print("Division List")
        print("=============================================================================\n")
        print(self.div)
        self.userDiv = str(input(f"What division would you like to display > ").title()) #Allows user to input division
        if self.userDiv in self.div: #If the user choice matches that of any value from division list
            userIn = str(input("Would you like to select a Party? (Y/N) > ").upper())
            if userIn == "Y":
                self.partyDivC()
            elif userIn == "N":
                for i in range(0, len(self.lines)): #For all lines
                    if str(self.lines[i].split(",")[2]) == self.userDiv: #If line division is equal to user input
                        self.divVal.insertLast(int(self.lines[i].split(",")[13])) #Insert votes from that line into list
                for val in self.divVal: #For each value in the list
                    self.divS += val #Sum the values
                print(f"Total accumulated votes: {self.divS} for the {self.userDiv} division") #Displays the accumulated votes for chosen division
                self.result.insertLast(self.userDiv) #Inserts user chosen division into a list
            else: #If input not recognized
                self.exit(1)
        else: #If input not recognized
            print("Party not in list of parties")
            print("Restarting part 3")
            return Margin()
        usercsv = str(input("Would you like to export the result as a CSV? (Y/N) > ").upper()) #Checks if user would like to export file as a CSV
        if usercsv == "Y":
            print("\n\nUnforunately this is useless due to the prior complications")
            self.exit(2)
            # return self.CSVexp()
        elif usercsv == "N":
            return self.exit(2)
        else: #If input not recognized
            return self.exit(1)

    def partyC(self):
        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        self.pty1 = str(input("Select first party comparison > ").upper())
        if self.pty1 in self.party: #If the user choice matches that of any value from party list
            userChoice = str(input("Would you like to select another party? (Y/N) > ").upper())
            if userChoice == "Y":
                self.party2()
            elif userChoice == "N":
                for i in range(0, len(self.lines)):
                    if str(self.lines[i].split(",")[11]) == self.pty1: #If line party is equal to user input
                        self.partyVal.insertLast(int(self.lines[i].split(",")[13])) #Insert votes from that line into list
                    elif str(self.lines[i].split(",")[11]) != self.pty1: #If line party is not equal to user input
                        self.otherVal.insertLast(int(self.lines[i].split(",")[13])) #Insert votes from that line into list
                for val in self.partyVal: #For each value in the list (user party choice)
                    self.partyS += val #Sum values
                for val in self.otherVal: #For each value in the list (other parties)
                    self.otherS += val #Sum values
                print(f"{self.pty1}: {self.partyS} Accumulated votes") #Displays chose party accumulated votes
                print(f"Other parties: {self.otherS} Accumulated votes") #Displays other parties accumulated votes
                print(f"Percent : {(self.partyS / (self.partyS+self.otherS)*100)} %") #Displays percentage difference
                self.margin = (self.partyS / (self.partyS+self.otherS))*100 - 50 #Calculates margin
                print(f"Margin : {(self.partyS / (self.partyS+self.otherS))*100 - 50}") #Displays margin difference
                self.marginComp()
        else: #If input not recognized
            print("Party not in list of parties")
            print("Restarting part 3")
            return Margin()
        usercsv = str(input("Would you like to export the result as a CSV? (Y/N) > ").upper()) #Checks if user would like to export file as a CSV
        if usercsv == "Y":
            print("\n\nUnforunately this is useless due to the prior complications")
            self.exit(2)
            # return self.CSVexp()
        elif usercsv == "N":
            return self.exit(2)
        else:
            return self.exit(1)

    def partyDivC(self):
        """Adaptation of first 2 parts"""


        print("\n=============================================================================")
        print("Party List")
        print("=============================================================================\n")
        print(self.party)
        self.pty1 = str(input("Select first party comparison > ").upper())
        if self.pty1 in self.party:
            userChoice = str(input("Would you like to select another party? (Y/N) > ").upper())
            if userChoice == "Y":
                self.partyDiv2()
            elif userChoice == "N":
                for i in range(0, len(self.lines)):
                    if str(self.lines[i].split(",")[11]) == self.pty1 and str(self.lines[i].split(",")[2]) == self.userDiv:
                        self.partyVal.insertLast(int(self.lines[i].split(",")[13]))
                    elif str(self.lines[i].split(",")[11]) != self.pty1 and str(self.lines[i].split(",")[2]) == self.userDiv:
                        self.otherVal.insertLast(int(self.lines[i].split(",")[13]))
                for val in self.partyVal:
                    self.partyS += val
                for val in self.otherVal:
                    self.otherS += val
                print(f"{self.pty1}: {self.partyS} Accumulated votes in the {self.userDiv} division")
                print(f"Other parties: {self.otherS} Accumulated votes in the {self.userDiv} division")
                print(f"Percent : {(self.partyS / (self.partyS+self.otherS)*100)} %")
                self.margin = (self.partyS / (self.partyS+self.otherS))*100 - 50
                print(f"Margin : {(self.partyS / (self.partyS+self.otherS))*100 - 50}")
                self.marginComp()
        else:
            print("Party not in list of parties")
            print("Restarting part 3")
            return Margin()
        usercsv = str(input("Would you like to export the result as a CSV? (Y/N) > ").upper())
        if usercsv == "Y":
            print("\n\nUnforunately this is useless due to the prior complications")
            self.exit(2)
            # return self.CSVexp()
        elif usercsv == "N":
            return self.exit(2)
        else:
            return self.exit(1)

    def party2(self):
        """Adaptation of single party, but accomodation for two party choices"""


        pty2 = str(input("Select second party comparison > ").upper())
        if pty2 in self.party:
            for i in range(0, len(self.lines)):
                if str(self.lines[i].split(",")[11]) == self.pty1:
                    self.partyVal.insertLast(int(self.lines[i].split(",")[13]))
                elif str(self.lines[i].split(",")[11]) == pty2:
                    self.party2Val.insertLast(int(self.lines[i].split(",")[13]))
            for val in self.partyVal:
                self.partyS += val
            for val in self.party2Val:
                self.party2S += val
            print(f"{self.pty1}: {self.partyS} Accumulated votes")
            print(f"{pty2}: {self.party2S} Accumulated votes")
            print(f"Percent : {(self.partyS / (self.partyS+self.party2S)*100)} %")
            self.margin = (self.partyS / (self.partyS+self.otherS))*100 - 50
            print(f"Margin : {(self.partyS / (self.partyS+self.party2S))*100 - 50}")
            self.marginComp()
        else:
            print("Party not in list of parties")
            print("Restarting part 3")
            Margin()
        usercsv = str(input("Would you like to export the result as a CSV? (Y/N) > ").upper())
        if usercsv == "Y":
            print("\n\nUnforunately this is useless due to the prior complications")
            self.exit(2)
            # self.CSVexp()
        elif usercsv == "N":
            self.exit(2)
        else:
            self.exit(1)

    def partyDiv2(self):
        """Adaptation of previous methods"""


        pty2 = str(input("Select second party comparison > ").upper())
        if pty2 in self.party:
            for i in range(0, len(self.lines)):
                if str(self.lines[i].split(",")[11]) == self.pty1 and str(self.lines[i].split(",")[2]) == self.userDiv:
                    self.partyVal.insertLast(int(self.lines[i].split(",")[13]))
                elif str(self.lines[i].split(",")[11]) == pty2 and str(self.lines[i].split(",")[2]) == self.userDiv:
                    self.party2Val.insertLast(int(self.lines[i].split(",")[13]))
            for val in self.partyVal:
                self.partyS += val
            for val in self.party2Val:
                self.party2S += val
            print(f"{self.pty1}: {self.partyS} Accumulated votes in the {self.userDiv} division")
            print(f"{pty2} {self.party2S} Accumulated votes in the {self.userDiv} division")
            print(f"Percent : {(self.partyS / (self.partyS+self.party2S)*100)} %")
            self.margin = (self.partyS / (self.partyS+self.party2S))*100 - 50
            print(f"Margin : {(self.partyS / (self.partyS+self.party2S))*100 - 50}")
            self.marginComp()
        else:
            print("Party not in list of parties")
            print("Restarting part 3")
            Margin()
        usercsv = str(input("Would you like to export the result as a CSV? (Y/N) > ").upper())
        if usercsv == "Y":
            print("\n\nUnforunately this is useless due to the prior complications")
            self.exit(2)
            # self.CSVexp()
        elif usercsv == "N":
            self.exit(2)
        else:
            self.exit(1)

    def exit(self, value):
        """General exit function based on where the error occured of what point they have reached of the program"""
        if value == 1:
            print("Command not recognized")
            user = str(input("Would you like to quit back to menu? (Y/N) > ").upper())
            if user == "Y":
                print("Thank you for playing, going back to menu")
                mn.Menu()
            elif user == "N":
                userC = str(input("Would you like to restart part 3? (Y/N) > ").upper())
                if userC == "Y":
                    print("restarting part 3".upper())
                    Margin()
                elif userC == "N":
                    print("Thank you for playing part 3, sending back to main menu")
                    mn.Menu()
                else:
                    print("command not recognized, sending back to main menu".upper())
                    mn.Menu()
            else:
                print("command not recognized, sending back to main menu".upper())
                mn.Menu()
        elif value == 2:
            print("Thank you for playing")
            user = str(input("Would you like to quit back to menu? (Y/N) > ").upper())
            if user == "Y":
                print("Thank you for playing, going back to menu")
                mn.Menu()
            elif user == "N":
                userC = str(input("Would you like to restart part 3? (Y/N) > ").upper())
                if userC == "Y":
                    print("restarting part 3".upper())
                    Margin()
                elif userC == "N":
                    print("Thank you for playing part 3, sending back to main menu")
                    mn.Menu()
                else:
                    print("command not recognized, sending back to main menu".upper())
                    mn.Menu()
            else:
                print("command not recognized, sending back to main menu".upper())
                mn.Menu()
        elif value == 3:
            userC = str(input("Would you like to return to the main menu? (Y/N) > ").upper())
            if userC == "Y":
                mn.Menu()
            elif userC == "N":
                print("Thank you for playing Candidate Selection 2016!")
                print("Note: We still know we are late on this")
            else:
                self.exit(1)

    def CSVexp(self):
        """Function to export file as a CSV"""
        myfile = open("Part3.csv", "w")
        for line in self.result: #For each line in list
            for item in line: #For each value
                myfile.write(item + ',') #Write it to a csv split by comma
            myfile.write('\n') #Newline for each line
        myfile.close() #Close file so it cannot be changed
        print(f"""
        CSV file saved under name Part1.csv. Thank you for playing Part 1!
        Sending back to Main Menu""")
        mn.Menu()

    def marginComp(self):
        if self.userVal is None: #If user did not choose to change marginal value
            if self.margin < self.default and self.margin > -self.default: #Does a comparison to see if margin is within default margin
                print(f"{self.margin}% is within the {self.default}% threshold")
                self.result.insertLast(self.partyS) #If it is insert party choice into a list
            elif self.margin > self.default and self.margin < -self.default: #If it's not in marginal range
                print(f"{self.margin}% is outside the {self.default}% threshold")
        elif self.userVal is not None: #If user changed marginal value
            if self.margin < self.userVal and self.margin > -self.userVal: #Does a comparison to see if margin is within default margin
                print(f"{self.margin}% is within the {self.userVal}% threshold")
                self.result.insertLast(self.partyS) #If it is insert party choice into a list
            elif self.margin > self.userVal or self.margin < -self.userVal: #If it's not in marginal range
                print(f"{self.margin}% is outside the {self.userVal}% threshold")
        else:
            print("I have no idea what happened")
        return self.result
