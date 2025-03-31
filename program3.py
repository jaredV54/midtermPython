from UserChoice import UserChoice  # Import the UserChoice function to handle user input for menu selections
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to ensure the user enters a valid monetary amount
from Currency import GetCryptoCurrencies  # Import to fetch conversion rates from physical currencies to cryptocurrencies

def Program3():
    while True:
        # Display the program title to indicate the current operation
        print("\n[--------- [ Forex Exchange Conversion ] ---------]\n")

        # Define a list of physical currencies available for conversion
        PHYSICAL_CURRENCIES = ["PHP", "USD", "AUD", "KRW", "JPY"]
        # Define a list of cryptocurrencies available for conversion
        CRYPTO_CURRENCIES = ["BTC", "SOL", "XRP", "ETH"]

        # Prompt the user to select a physical currency from the list
        print("Select a Physical Currency:")
        for i in range(1, 6):
            # Display each physical currency option with a corresponding number
            print(f"{i}. {PHYSICAL_CURRENCIES[i - 1]}")
        # Provide an option to cancel the selection process
        print(f"6. Cancel\n")

        # Get the user's choice for the physical currency using the UserChoice function
        physicalCurrency = UserChoice(6)
        if physicalCurrency == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break

        # Prompt the user to select a cryptocurrency from the list
        print("\nSelect a Crypto Currency:")
        for i in range(1, 5):
            # Display each cryptocurrency option with a corresponding number
            print(f"{i}. {CRYPTO_CURRENCIES[i - 1]}")
        # Provide an option to cancel the selection process
        print(f"5. Cancel\n")

        # Get the user's choice for the cryptocurrency using the UserChoice function
        crytoCurrency = UserChoice(5)
        if crytoCurrency == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break

        # Determine the names of the chosen physical and cryptocurrency based on user input
        source = PHYSICAL_CURRENCIES[physicalCurrency - 1]
        target = CRYPTO_CURRENCIES[crytoCurrency - 1]
        # Prompt the user to enter an amount in the chosen physical currency
        amount = AmountInPhysicalCurrency(source)

        # Display a message indicating that the conversion process is underway
        print("\n[--------------- [ Processing... ]---------------]\n")

        # Fetch the conversion rates for the selected physical and cryptocurrency
        prices = GetCryptoCurrencies(source, target, amount)
        if not prices:
            # If there was an error retrieving prices, restart the loop to try again
            continue
        
        # Display the original amount in the physical currency
        print(f"{source}: {prices['amount']}")
        # Display the converted amount in the chosen cryptocurrency
        print(f"{target}: {prices['result'][target]}")
        # Display the conversion rate used for the transaction
        print(f"Rate: {prices['result']['rate']}")
        # Exit the loop after successfully completing one conversion
        break