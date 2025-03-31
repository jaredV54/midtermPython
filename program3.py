from UserChoice import UserChoice  # Import the UserChoice function to get user input
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to get a valid amount from the user
from Currency import GetCryptoCurrencies  # Import to fetch cryptocurrency conversion rates

def Program3():
    while True:
        # Display the program title
        print("\n[--------- [ Forex Exchange Conversion ] ---------]\n")

        # List of physical currencies you can choose from
        PHYSICAL_CURRENCIES = ["PHP", "USD", "AUD", "KRW", "JPY"]
        # List of cryptocurrencies you can choose from
        CRYPTO_CURRENCIES = ["BTC", "SOL", "XRP", "ETH"]

        # Ask the user to select a physical currency
        print("Select a Physical Currency:")
        for i in range(1, 6):
            # Show each physical currency with a number
            print(f"{i}. {PHYSICAL_CURRENCIES[i - 1]}")
        # Option to cancel the selection
        print(f"6. Cancel\n")

        # Get the user's choice for the physical currency
        physicalCurrency = UserChoice(6)
        if physicalCurrency == "break":
            # If the user cancels, exit the loop
            break

        # Ask the user to select a cryptocurrency
        print("\nSelect a Crypto Currency:")
        for i in range(1, 5):
            # Show each cryptocurrency with a number
            print(f"{i}. {CRYPTO_CURRENCIES[i - 1]}")
        # Option to cancel the selection
        print(f"5. Cancel\n")

        # Get the user's choice for the cryptocurrency
        crytoCurrency = UserChoice(5)
        if crytoCurrency == "break":
            # If the user cancels, exit the loop
            break

        # Get the names of the chosen physical and crypto currencies
        source = PHYSICAL_CURRENCIES[physicalCurrency - 1]
        target = CRYPTO_CURRENCIES[crytoCurrency - 1]
        # Ask the user to enter an amount in the chosen physical currency
        amount = AmountInPhysicalCurrency(source)

        # Display a processing message
        print("\n[--------------- [ Processing... ]---------------]\n")

        # Get the conversion rates for the chosen currencies
        prices = GetCryptoCurrencies(source, target, amount)
        if not prices:
            # If there was an error getting prices, start over
            continue
        
        # Display the amount in the physical currency
        print(f"{source}: {prices['amount']}")
        # Display the amount in the crypto currency
        print(f"{target}: {prices['result'][target]}")
        # Display the conversion rate
        print(f"Rate: {prices['result']['rate']}")
        # Exit the loop after one conversion
        break