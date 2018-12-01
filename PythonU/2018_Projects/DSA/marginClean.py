from linkedList import *
import csv
import menu as mn

class Margin:
    def __init__(self, margin = 6):
        print("\nWelcome to Margin selection, here you will select a party and a marginal value selection. \nIf a party is within the marginal value in any division, it is added to a seperate list.")
        loadpath = "C:/Users/Gabriel/Desktop/University/2ndYear/Semester2/COMP1002/Assignment"
        # self.path = loadpath + "/HouseStateFirstPrefsByPollingPlaceDownload-20499-ACT.csv"
        self.path = loadpath + "/margin.csv"
        self.state = DSALinkedList()
        self.party = DSALinkedList()
        self.div = DSALinkedList()
        self.parti = DSALinkedList()
        self.divU = DSALinkedList()
        self.partyN = DSALinkedList()
        with open(self.path, 'r') as csvfile:
            data = csv.reader(csvfile, delimiter = ',')
            next(data)
            next(data)
            self.value = [row for row in data]
            for row in self.value:
                if row[2] not in self.div:
                    self.div.insertLast(row[2])
            for row in self.value:
                if row[11] not in self.parti:
                    self.parti.insertLast(row[11])
            # print(self.div)
                # if row[11] not in self.party or row[12] not in self.party:
                #     self.party.insertLast(row[12])
                #     self.party.insertLast(row[11])
                    # self.party.insertLast(row[12])
        self.userVal = None
        self.default = margin
        user = str(input("Would you like to change the margin value from the default 6%? (Y/N) > ").upper())
        if user == "Y":
            self.userVal = float(input("Select margin to use > "))
        elif user == "N":
            pass
        else:
            print("\nInput not recognised, returning to menu\n")
            mn.Menu()
        self.result = DSALinkedList()
        # self.result = []
        self.other = DSALinkedList()
        self.votesFor = {}
        self.votesAgainst = {}
        print(self.parti)
        self.userPty = str(input("Select Party > ").upper())
        if self.userPty in self.parti:
            for val in self.value:
                for self.loc in self.div:
                    if str(val[11]) == self.userPty and val[2] == self.loc:
                        self.result.insertLast(((val[0], val[2], val[11]), int(val[13])))
                    elif str(val[11]) != self.userPty and val[2] == self.loc:
                        self.other.insertLast(((val[0], val[2], val[11]), int(val[13])))
        else:
            print("\nParty not found, returning to menu\n")
            mn.Menu()
        self.marginVotes()

    # def selfR(self):
    #     print(self.votesFor)

    def marginVotes(self, margin = 6):
        self.marginResult = DSALinkedList()
        for key,value in self.result:
            if key in self.votesFor:
                self.votesFor[key] += value
            else:
                self.votesFor[key] = value
        for key,value in self.other:
            if key in self.votesAgainst:
                self.votesAgainst[key] += value
            else:
                self.votesAgainst[key] = value

        for k, v in self.votesFor.items():
            for self.key, value in self.votesAgainst.items():
                if self.key[1] == k[1]:
                    self.margin = (v / (v+value))*100 - 50
                    if self.userVal is None:
                        if self.margin < self.default and self.margin > -self.default:
                            if (self.key[0], self.key[1]) not in self.marginResult:
                                self.marginResult.insertLast((self.key[0], self.key[1]))
                    elif self.userVal is not None:
                        if self.margin < self.userVal and self.margin > -self.userVal:
                            if (self.key[0], self.key[1]) not in self.marginResult:
                                self.marginResult.insertLast((self.key[0], self.key[1]))

        print("""What would you like to do? \n
                1. Display Results
                2. Write results to a csv
                3. Exit program?
                 """)
        user = int(input("Select choice > "))
        if user == 1:
            self.displayR()
        elif user == 2:
            self.writeCSV()
        elif user == 3:
            print("Thank you for playing!")
            mn.Menu()
        else:
            userC = str(input("Whoops your choice was not recognised, would you like to try again? (Y/N) > ").upper())
            if userC == "Y":
                self.marginVotes()
            elif userC == "N":
                print("Thank you for playing!")
                mn.Menu()
            else:
                print("It appears your choice was not recognised again, so we will assume you would like to quit \n Thank you for playing!")
                mn.Menu()

    def displayR(self):
        for i in self.marginResult:
            print(i)
        print("Keep in mind CSV is necessary for creating itinerary")
        user = str(input("Would you like to save the results as a CSV? (Y/N) > ").upper())
        if user == "Y":
            self.writeCSV()
        elif user == "N":
            print("Thank you for playing!")
            mn.Menu()
        else:
            userC = str(input("Whoops your choice was not recognised, would you like to try again? (Y/N) > ").upper())
            if userC == "Y":
                self.displayR()
            elif userC == "N":
                print("Thank you for playing!")
                mn.Menu()
            else:
                print("It appears your choice was not recognised again, so we will assume you would like to quit \n Thank you for playing!")
                mn.Menu()

    def writeCSV(self):
        #userFile = str(input("What would you like the file to be called? > "))
        with open("Part3.csv", 'w', newline='') as myfile: #Creates input file according to what user called it
            wr = csv.writer(myfile) #Allows the file to open to writing
            for line in self.marginResult:
                wr.writerow(line) #Write each line of sorted list into the csv file
            myfile.close()
        print(f"""
        CSV file saved under name Part3.csv. Thank you for playing Part 3!
        Sending back to Main Menu""")
        mn.Menu()

# m = Margin()
# m.split()


# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row/3348664
# https://stackoverflow.com/questions/32004774/sum-multiple-values-for-same-key-in-lists-using-python
