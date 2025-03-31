from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to ensure the user enters a valid monetary amount
from UserChoice import UserChoice  # Import to handle user input for menu selections

def Program2():
    while True:
        # Define a list of digital payment platforms available for conversion
        PLATFORMS = ["PayPal", "GCash", "PayMaya", "Bank"]

        # Display the program title to indicate the current operation
        print("\n[--- [PHP Digital Payment Platform Conversion] ---]\n")
        
        # Prompt the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")

        # Prompt the user to select a source platform from the list
        print("\nSelect a source platform:")
        for i in range(len(PLATFORMS)):
            # Display each platform option with a corresponding number
            print(f"{i + 1}. {PLATFORMS[i]}")
        # Provide an option to cancel the selection process
        print("5. Cancel\n")

        # Get the user's choice for the source platform using the UserChoice function
        sourceChoice = UserChoice(5)
        if sourceChoice == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break
        print("\n[------------------------------------------------]\n")

        # Prompt the user to select a target platform from the list
        print("Select a target platform:")
        for i in range(len(PLATFORMS)):
            # Display each platform option with a corresponding number
            print(f"{i + 1}. {PLATFORMS[i]}")
        # Provide an option to cancel the selection process
        print("5. Cancel\n")

        # Get the user's choice for the target platform using the UserChoice function
        targetChoice = UserChoice(5)
        if targetChoice == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break
        print("\n[------------------------------------------------]\n")
        
        # Determine the names of the chosen source and target platforms based on user input
        source = PLATFORMS[sourceChoice - 1]
        target = PLATFORMS[targetChoice - 1]

        # Display the conversion direction from source to target platform
        print((f"{source} to {target}\n").upper())

        # Convert the amount and calculate any applicable transaction fees
        converted = convertToDigitalPlatform(amount, source, target)
        # Display the total amount to be paid, including fees
        print(f"Amount to pay: {converted:.2f}₱")
        # Display the amount the target platform receives
        print(f"Amount they receive: {amount:.2f}₱")
        
        # Exit the loop after successfully completing one conversion
        break  

def convertToDigitalPlatform(amount, source, target):
    # Define the transaction fee rates for each platform
    fees = {
        "PayPal": 0.029,   # PayPal fee rate
        "GCash": 0.02,     # GCash fee rate
        "PayMaya": 0.02,   # PayMaya fee rate
        "Bank": 0.015      # Bank fee rate for same-bank transfers
    }
    
    # Check if the source and target platforms are the same
    isSamePlatform = source == target
    
    # Determine the fee rate based on whether platforms are the same
    feeRate = 0.0 if isSamePlatform else fees[target]
    # Calculate the fee amount based on the fee rate
    feeAmount = amount * feeRate
    # Calculate the total amount to be paid, including the fee
    totalAmount = amount + feeAmount
    if isSamePlatform:
        # If transferring within the same platform, there is no fee
        print(f"There is no charge :)")
    else:
        # Display the transaction fee details for the conversion
        print(f"Transaction fee for {source}: {(fees[source] * 100):.1f}%")
        print(f"PHP: {amount:.2f}₱")
        print(f"Fee: {feeAmount:.2f}₱\n")
    
    # Return the total amount to be paid, including any fees
    return totalAmount