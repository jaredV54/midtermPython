from Currency import GetExchangeRatePerYear, GetCurrencyOptions  # Import functions to get exchange rates and currency options
from AmountInPhysicalCurrency import AmountInPhysicalCurrency  # Import to get a valid amount from the user
from UserChoice import UserChoice  # Import to get user input

def Program4():
    while True:
        # Retrieve the average exchange rates for each year from the Currency module
        exchangeRatePerYear = GetExchangeRatePerYear()
        # Retrieve the currency options and their symbols from the Currency module
        currencyOptions = GetCurrencyOptions()
        # Define a list of years for which exchange rates are available
        YEARS = ["2021", "2022", "2023", "2024"]

        # Display the program title to the user
        print("\n[----- [ PHP Yearly Average Exchange Rate  ] -----]")
        # Prompt the user to select a year for which they want to see exchange rates
        print("\nSelect year:")
        for i in range(len(YEARS)):
            # Display each year as an option with a corresponding number
            print(f"{i + 1}. {YEARS[i]}")
        # Provide an option to cancel the selection process
        print("5. Cancel\n")

        # Get the user's choice for the year using the UserChoice function
        choice = UserChoice(5)
        if choice == "break":
            # If the user chooses to cancel, exit the loop and end the program
            break
        
        # Prompt the user to enter an amount in PHP currency
        amount = AmountInPhysicalCurrency("PHP")
        # Display a separator line for better readability
        print("\n[------------------------------------------------]")
        
        # Retrieve the exchange rates for the year selected by the user
        selectedYear = exchangeRatePerYear[YEARS[choice - 1]] 
        # Display the entered amount in PHP along with the selected year
        print(f"\n{amount:.2f}₱ amount in year {YEARS[choice - 1]}:")
        
        # Define a list of physical currencies to which the PHP amount can be converted
        PHYSICAL_CURRENCIES = ["USD", "AUD", "KRW", "JPY"]
        for i in range(len(PHYSICAL_CURRENCIES)):
            # Get the currency code and its corresponding exchange rate
            currency = PHYSICAL_CURRENCIES[i]
            value = selectedYear[currency]
            # Calculate and display the converted amount in each currency
            print(f"{currency}: {(value * amount):.2f}{currencyOptions[i + 1][1]}")
        
        # Exit the loop after performing one conversion
        break