def UserChoice(maxVal, isMain = False):
        minVal = 1
        validRange = range(minVal, maxVal + 1)

        try:
            choice = int(input(f"Enter your choice ({minVal}-{maxVal}): "))
            if choice == maxVal:
                if  isMain:
                     print("\n[----- [ Exiting the program. Goodbye! ] -----]\n")
                else: 
                     print("\n[------------ [ Program Canceled ] ------------]")  
                return "break"
            if choice not in validRange:
                print(f"Oh noo! That option is out of range. Please enter a number between {minVal} and {maxVal}.")
                return "continue"
        except ValueError:
            print(f"Invalid input! Please enter a numeric value between {minVal} and {maxVal}.")
            return "continue"
        return choice
