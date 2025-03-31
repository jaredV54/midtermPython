from program1 import Program1
from program2 import Program2
from program3 import Program3
from program4 import Program4
from UserChoice import UserChoice

def main():
    while True:
        # Display the main menu options
        print("\n[------------------[ Main Menu ]-----------------]\n")
        print("Please choose your conversion:")
        print("1. PHP Currency Exchange")
        print("2. PHP Digital Payment Platform")
        print("3. Forex Exchange Conversion")
        print("4. PHP Yearly Average Exchange Rate")
        print("5. Exit\n")

        # Ask the user to choose an option from the main menu
        choice = UserChoice(5, True)
        if choice == "break":
            # If the user chooses to exit, break the loop
            break
        elif choice == "continue":
            # If the user chooses an invalid option, continue the loop
            continue

        # Call the function to handle the chosen conversion
        chooseConversion(choice)
        
def chooseConversion(choice):
    # Check which conversion program to run based on user choice
    if choice == 1:
        Program1()
    elif choice == 2:
        Program2()
    elif choice == 3:
        Program3()
    elif choice == 4:
        Program4()

    while True:
        # Ask the user what they want to do next
        print("\nChoose your next action (1-3):")
        print("1. Convert again with the same program")
        print("2. Change program")
        print("3. Exit\n")

        # Get the user's choice for the next action
        nextActionChoice = UserChoice(3, True)
        if nextActionChoice == "continue":
            # If the user chooses an invalid option, continue the loop
            continue
        elif nextActionChoice == 1:
            # If the user wants to convert again, call the same conversion function
            chooseConversion(choice)

        # Exit the loop if the user chooses to change program or exit
        break

# Check if this script is being run directly
if __name__ == "__main__":
    # Start the main function
    main()