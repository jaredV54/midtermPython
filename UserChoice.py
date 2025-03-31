import sys  # Import the sys module to use system-specific parameters and functions, such as exiting the program

def UserChoice(maxVal, isMain=False):
    # This function prompts the user to make a choice from a menu
    # maxVal: the maximum valid choice number
    # isMain: a boolean indicating if this is the main menu (affects exit behavior)

    # Set the minimum valid choice value
    minVal = 1
    # Create a range of valid choices from minVal to maxVal, inclusive
    validRange = range(minVal, maxVal + 1)

    while True:
        # This loop will continue until the user provides a valid input
        try:
            # Ask the user to enter their choice, displaying the valid range
            choice = int(input(f"Enter your choice ({minVal}-{maxVal}): "))
            if choice == maxVal:
                # If the choice is the maximum value, check if it's the main menu
                if isMain:
                    # If it's the main menu, print an exit message and close the program
                    print("\n[------- [ Exiting the program. Goodbye!] -------]\n")
                    sys.exit()  # Exit the program immediately
                else:
                    # If it's not the main menu, print a cancellation message
                    print("\n[------------- [ Program Canceled ] -------------]")  
                # Return "break" to indicate the user wants to cancel the current operation
                return "break"
            if choice not in validRange:
                # If the choice is not within the valid range, print an error message
                print(f"Oh noo! That option is out of range. Please enter a number between {minVal} and {maxVal}.")
                # Continue the loop to prompt the user again
                continue
        except ValueError:
            # If the user enters a non-numeric value, catch the error and print an error message
            print(f"Invalid input! Please enter a numeric value between {minVal} and {maxVal}.")
            # Continue the loop to prompt the user again
            continue
        # If the input is valid, return the user's choice
        return choice