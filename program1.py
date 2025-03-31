from Currency import GetExchangeRate, GetCurrencyOptions  # Import functions to get exchange rates and currency options
from UserChoice import UserChoice  # Import to get user input
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to get a valid amount from the user

def Program1():
    while True:
        # Get the currency options and their symbols
        currencyOptions = GetCurrencyOptions()

        # Display the program title
        print("\n[-------- [ PHP Currency Exchange Menu ] --------]\n")
        # Ask the user to select a currency to convert to
        for i in range(1, 5):
            code, symbol, _ = currencyOptions[i]
            # Show each currency with its symbol
            print(f"{i}. {code} ({symbol})")
        # Option to cancel the selection
        print("5. Cancel\n")
 
        # Get the user's choice for the currency
        choice = UserChoice(5)
        if choice == "break":
            # If the user cancels, exit the loop
            break
        
        # Ask the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")
        # Display a processing message
        print("\n[--------------- [ Processing... ]---------------]\n")

        # Get the latest exchange rates
        exchangeRates = GetExchangeRate()
        # Get the chosen currency's code, symbol, and denominations
        currencyCode, symbol, denominations = currencyOptions[choice]
        # Calculate the converted amount
        converted = amount * exchangeRates[currencyCode]

        # Find the smallest denomination for rounding
        smallestDenomination = min(denominations)
        # Round the converted amount to the nearest smallest denomination
        converted = round(converted / smallestDenomination) * smallestDenomination

        # Display the converted amount with the correct symbol
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
        
        # Exit the loop after one conversion
        break  
            
def breakdownAmount(amount, denominations):
    # Create a dictionary to store the breakdown of the amount
    breakdown = {}
    # Start with the full amount to be broken down
    remaining = amount

    # Go through each denomination
    for denom in denominations:
        # Calculate how many of this denomination fit into the remaining amount
        count = int(remaining // denom)
        if count > 0:
            # If any fit, add them to the breakdown
            breakdown[denom] = count
            # Subtract the value of these denominations from the remaining amount
            remaining = round(remaining - denom * count, 2) 
    # Return the breakdown of the amount
    return breakdown