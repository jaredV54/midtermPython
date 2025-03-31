from program1 import Program1  # Import the Program1 function to handle PHP currency exchange
from program2 import Program2  # Import the Program2 function for digital payment platform conversion
from program3 import Program3  # Import the Program3 function for forex exchange conversion
from program4 import Program4  # Import the Program4 function for yearly average exchange rate
from UserChoice import UserChoice  # Import the UserChoice function to get user input

def main():
    while True:
        # This is the main function that will keep running until the user decides to exit
        # The while loop allows the program to continuously prompt the user for actions
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
            # If the user chooses to exit, break the loop and end the program
            break
        elif choice == "continue":
            # If the user chooses an invalid option, continue the loop to ask again
            continue

        # Call the function to handle the chosen conversion
        chooseConversion(choice)
        
def chooseConversion(choice):
    # This function decides which conversion program to run based on the user's choice
    if choice == 1:
        Program1()  # Run the PHP Currency Exchange program
    elif choice == 2:
        Program2()  # Run the Digital Payment Platform Conversion program
    elif choice == 3:
        Program3()  # Run the Forex Exchange Conversion program
    elif choice == 4:
        Program4()  # Run the Yearly Average Exchange Rate program

    while True:
        # After a conversion is done, ask the user what they want to do next
        print("\nChoose your next action (1-3):")
        print("1. Convert again with the same program")
        print("2. Change program")
        print("3. Exit\n")

        # Get the user's choice for the next action
        nextActionChoice = UserChoice(3, True)
        if nextActionChoice == "continue":
            # If the user chooses an invalid option, continue the loop to ask again
            continue
        elif nextActionChoice == 1:
            # If the user wants to convert again with the same program, call chooseConversion again
            # This is a form of recursion where the function calls itself
            chooseConversion(choice)

        # Exit the loop if the user chooses to change program or exit
        break

# Check if this script is being run directly
if __name__ == "__main__":
    # If this script is run directly (not imported), start the main function
    main()