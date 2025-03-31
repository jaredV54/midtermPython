import sys  # Import the sys module to use system-specific parameters and functions

def UserChoice(maxVal, isMain=False):
    # Set the minimum valid choice value
    minVal = 1
    # Create a range of valid choices from minVal to maxVal
    validRange = range(minVal, maxVal + 1)

    while True:
        try:
            # Ask the user to enter their choice
            choice = int(input(f"Enter your choice ({minVal}-{maxVal}): "))
            if choice == maxVal:
                # If the choice is the maximum value, check if it's the main menu
                if isMain:
                    # If it's the main menu, print an exit message and close the program
                    print("\n[------- [ Exiting the program. Goodbye!] -------]\n")
                    sys.exit()
                else:
                    # If it's not the main menu, print a cancellation message
                    print("\n[------------- [ Program Canceled ] -------------]")  
                # Return "break" to indicate the user wants to cancel
                return "break"
            if choice not in validRange:
                # If the choice is not in the valid range, print an error message
                print(f"Oh noo! That option is out of range. Please enter a number between {minVal} and {maxVal}.")
                continue
        except ValueError:
            # If the user enters a non-numeric value, print an error message
            print(f"Invalid input! Please enter a numeric value between {minVal} and {maxVal}.")
            continue
        # Return the user's valid choice
        return choice