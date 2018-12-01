import substring as sub
#import margin as marg
import filter as flt
import itinerary as quarter
import marginClean as marg

class Menu():
    def __init__(self):
        print("=============================================================================")
        print("Welcome to the Candidate Selection of 2016! (Yes we know we are a bit late)")
        print("=============================================================================")
        print("\nWhat would you like to do")
        print("""
        1. List all participating Nominees
        2. Search by Nominee
        3. List by marginal seat
        4. Itinerary by Margin
        0. Quit the candidate selection\n""")

        user = str(input("Select what you would like to do > "))

        if user == "1":
            flt.State()
        elif user == "2":
            sub.Sub()
        elif user ==  "3":
            marg.Margin()
        elif user == "4":
            quarter.Iti()
        elif user == "0":
            print("We will hopefully be more up to date next time")
            print("Thank you for running the program!")
        else:
            print("USER ERROR PLEASE TRY AGAIN")
            Menu()

if __name__ == '__main__':
    Menu()
