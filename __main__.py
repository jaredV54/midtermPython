from program1 import Program1
from program2 import Program2
from program3 import Program3
from program4 import Program4
from UserChoice import UserChoice

def main():
    while True:
        print("\n[------------------[ Main Menu ]-----------------]\n")
        print("Please choose your conversion:")
        print("1. Currency Exchange")
        print("2. Digital Payment Platform")
        print("3. Program3")
        print("4. Check PHP Average Exchange Rate Per Year")
        print("5. Exit\n")

        choice = UserChoice(5, True)
        if choice == "break":
            break
        elif choice == "continue":
            continue

        isBreak = chooseConversion(choice)
        if isBreak == "break":
            break
        
def chooseConversion(choice):
    if choice == 1:
        Program1()
    elif choice == 2:
        Program2()
    elif choice == 3:
        Program3()
    elif choice == 4:
        Program4()

    while True:
        print("\nChoose your next action (1-3):")
        print("1. Convert again with the same program")
        print("2. Change program")
        print("3. Exit\n")

        nextActionChoice = UserChoice(3, True)
        if nextActionChoice == "break":
            return nextActionChoice
        elif nextActionChoice == "continue":
            continue
        elif nextActionChoice == 1:
            chooseConversion(choice)

        break

if __name__ == "__main__":
    main()
