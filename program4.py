from Currency import GetExchangeRatePerYear, GetCurrencyOptions  # Import functions to get exchange rates and currency options
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to get a valid amount from the user
from UserChoice import UserChoice  # Import to get user input

def Program4():
    while True:
        # Get the average exchange rates for each year
        exchangeRatePerYear = GetExchangeRatePerYear()
        # Get the currency options and their symbols
        currencyOptions = GetCurrencyOptions()
        # List of years to choose from
        YEARS = ["2021", "2022", "2023", "2024"]

        # Display the program title
        print("\n[----- [ PHP Yearly Average Exchange Rate  ] -----]")
        # Ask the user to select a year
        print("\nSelect year:")
        for i in range(len(YEARS)):
            # Show each year with a number
            print(f"{i + 1}. {YEARS[i]}")
        # Option to cancel the selection
        print("5. Cancel\n")

        # Get the user's choice for the year
        choice = UserChoice(5)
        if choice == "break":
            # If the user cancels, exit the loop
            break
        
        # Ask the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")
        # Display a separator line
        print("\n[------------------------------------------------]")
        
        # Get the exchange rates for the selected year
        selectedYear = exchangeRatePerYear[YEARS[choice - 1]] 
        # Display the amount in PHP for the selected year
        print(f"\n{amount:.2f}₱ amount in year {YEARS[choice - 1]}:")
        
        # List of physical currencies to convert to
        PHYSICAL_CURRENCIES = ["USD", "AUD", "KRW", "JPY"]
        for i in range(len(PHYSICAL_CURRENCIES)):
            # Get the currency and its exchange rate
            currency = PHYSICAL_CURRENCIES[i]
            value = selectedYear[currency]
            # Display the converted amount in each currency
            print(f"{currency}: {(value * amount):.2f}{currencyOptions[i + 1][1]}")
        
        # Exit the loop after one conversion
        break