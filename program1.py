from Currency import GetExchangeRate, GetCurrencyOptions  # Import functions to get exchange rates and currency options
from UserChoice import UserChoice  # Import to get user input
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to get a valid amount from the user

def Program1():
    while True:
        # Retrieve the available currency options and their symbols
        currencyOptions = GetCurrencyOptions()

        # Display the program title to indicate the current operation
        print("\n[-------- [ PHP Currency Exchange Menu ] --------]\n")
        # Prompt the user to select a currency to convert to
        for i in range(1, 5):
            code, symbol, _ = currencyOptions[i]
            # Display each currency option with its symbol
            print(f"{i}. {code} ({symbol})")
        # Provide an option to cancel the selection process
        print("5. Cancel\n")
 
        # Get the user's choice for the currency using the UserChoice function
        choice = UserChoice(5)
        if choice == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break
        
        # Prompt the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")
        # Display a message indicating that the conversion process is underway
        print("\n[--------------- [ Processing... ]---------------]\n")

        # Retrieve the latest exchange rates from the Currency module
        exchangeRates = GetExchangeRate()
        # Get the chosen currency's code, symbol, and denominations
        currencyCode, symbol, denominations = currencyOptions[choice]
        # Calculate the converted amount using the exchange rate
        converted = amount * exchangeRates[currencyCode]

        # Find the smallest denomination for rounding purposes
        smallestDenomination = min(denominations)
        # Round the converted amount to the nearest smallest denomination
        converted = round(converted / smallestDenomination) * smallestDenomination

        # Display the converted amount with the appropriate currency symbol
        print("Converted amount:", end=" ")
        print(f"{symbol}{converted:.2f}" if currencyCode in ['USD', 'AUD'] else f"{symbol}{converted} {currencyCode}")

        # Get the breakdown of the converted amount into denominations
        breakdown = breakdownAmount(converted, denominations)
        # Display the breakdown of the amount
        print("\nBreakdown:")
        for denom in breakdown:
            count = breakdown[denom]
            # Display each denomination with its count
            if currencyCode in ["USD", "AUD"]:
                print(f"{count} x " + f"{int(denom * 100)}¢" if denom < 1 else f"{count} x {denom}$")
            else:
                print(f"{count} x {symbol}{denom}")
        
        # Exit the loop after successfully completing one conversion
        break  
            
def breakdownAmount(amount, denominations):
    # Create a dictionary to store the breakdown of the amount into denominations
    breakdown = {}
    # Start with the full amount to be broken down
    remaining = amount

    # Iterate over each denomination to calculate how many fit into the remaining amount
    for denom in denominations:
        # Determine how many of this denomination fit into the remaining amount
        count = int(remaining // denom)
        if count > 0:
            # If any fit, add them to the breakdown dictionary
            breakdown[denom] = count
            # Subtract the value of these denominations from the remaining amount
            remaining = round(remaining - denom * count, 2) 
    # Return the breakdown of the amount as a dictionary
    return breakdown