from AmountInPhysicalCurrency import AmountInPhysicalCurrency
from UserChoice import UserChoice

def Program2():
    while True:
        # List of platforms you can choose from
        PLATFORMS = ["PayPal", "GCash", "PayMaya", "Bank"]

        # Display the program title
        print("\n[--- [PHP Digital Payment Platform Conversion] ---]\n")
        
        # Ask the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")

        # Ask the user to select a source platform
        print("\nSelect a source platform:")
        for i in range(len(PLATFORMS)):
            # Show each platform with a number
            print(f"{i + 1}. {PLATFORMS[i]}")
        # Option to cancel the selection
        print("5. Cancel\n")

        # Get the user's choice for the source platform
        sourceChoice = UserChoice(5)
        if sourceChoice == "break":
            # If the user cancels, exit the loop
            break
        print("\n[------------------------------------------------]\n")

        # Ask the user to select a target platform
        print("Select a target platform:")
        for i in range(len(PLATFORMS)):
            # Show each platform with a number
            print(f"{i + 1}. {PLATFORMS[i]}")
        # Option to cancel the selection
        print("5. Cancel\n")

        # Get the user's choice for the target platform
        targetChoice = UserChoice(5)
        if targetChoice == "break":
            # If the user cancels, exit the loop
            break
        print("\n[------------------------------------------------]\n")
        
        # Get the names of the chosen source and target platforms
        source = PLATFORMS[sourceChoice - 1]
        target = PLATFORMS[targetChoice - 1]

        # Display the conversion direction
        print((f"{source} to {target}\n").upper())

        # Convert the amount and calculate fees
        converted = convertToDigitalPlatform(amount, source, target)
        # Show the total amount to pay
        print(f"Amount to pay: {converted:.2f}₱")
        # Show the amount the target receives
        print(f"Amount they receive: {amount:.2f}₱")
        
        # Exit the loop after one conversion
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
    # Calculate the fee amount
    feeAmount = amount * feeRate
    # Calculate the total amount including fees
    totalAmount = amount + feeAmount
    if isSamePlatform:
        # No fee if transferring within the same platform
        print(f"There is no charge :)")
    else:
        # Show the transaction fee details
        print(f"Transaction fee for {source}: {(fees[source] * 100):.1f}%")
        print(f"PHP: {amount:.2f}₱")
        print(f"Fee: {feeAmount:.2f}₱\n")
    
    # Return the total amount to be paid
    return totalAmount