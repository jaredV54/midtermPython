from Currency import GetExchangeRatePerYear, GetCurrencyOptions
from Amount import AmountInPhysicalCurrency
from UserChoice import UserChoice
def Program4():
    while True:
        exchangeRatePerYear = GetExchangeRatePerYear()
        currencyOptions = GetCurrencyOptions()
        YEARS = ["2021", "2022", "2023", "2024"]

        print("\n[----- [ PHP Yearly Average Exchange Rate  ] -----]")
        print("\nSelect year:")
        for i in range(len(YEARS)):
            print(f"{i + 1}. {YEARS[i]}")
        print("5. Cancel\n")

        choice = UserChoice(5)
        if choice == "break":
            break
        
        amount = AmountInPhysicalCurrency("PHP")
        print("\n[------------------------------------------------]")
        
        selectedYear = exchangeRatePerYear[YEARS[choice - 1]] 
        print(f"\n{amount:.2f}₱ amount in year {YEARS[choice - 1]}:")
        
        PHYSICAL_CURRENCIES = ["USD", "AUD", "KRW", "JPY"]
        for i in range(len(PHYSICAL_CURRENCIES)):
            currency = PHYSICAL_CURRENCIES[i]
            value = selectedYear[currency]
            print(f"{currency}: {(value * amount):.2f}{currencyOptions[i + 1][1]}")
        
        break  
