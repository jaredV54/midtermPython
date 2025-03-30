from program1 import Program1
from program2 import Program2
from program3 import Program3
from program4 import Program4
from UserChoice import UserChoice

def main():
    while True:
        print("\n[------------------[ Main Menu ]-----------------]\n")
        print("Please choose your conversion:")
        print("1. PHP Currency Exchange")
        print("2. PHP Digital Payment Platform")
        print("3. Forex Exchange Conversion")
        print("4. PHP Yearly Average Exchange Rate")
        print("5. Exit\n")

        choice = UserChoice(5, True)
        if choice == "break":
            break
        elif choice == "continue":
            continue

        chooseConversion(choice)
        
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
        if nextActionChoice == "continue":
            continue
        elif nextActionChoice == 1:
            chooseConversion(choice)

        break

if __name__ == "__main__":
    main()
