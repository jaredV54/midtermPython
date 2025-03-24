from Currency import GetExchangeRatePerYear, GetCurrencyOptions
from AmountInPHP import AmountInPHP
from UserChoice import UserChoice

def Program4():
    exchangeRatePerYear = GetExchangeRatePerYear()
    currencyOptions = GetCurrencyOptions()
    years = ["2021", "2022", "2023", "2024"]

    print("\n[ - [ Check PHP Average Exchange Rate Per Year ] - ]")
    print("\nSelect year:")
    for i, year in enumerate(years):
        print(f"{i + 1}. {year}")
    print("5. Choose another action\n")

    choice = UserChoice(5, Program4)
    if choice is None:
        return None
    
    amount = AmountInPHP(Program4)
    if amount is None:
        return None
    print("[------------------------------------------------]")
    
    selectedYear = exchangeRatePerYear[years[choice - 1]] 

    print(f"\n{amount:.2f}₱ amount in year {years[choice - 1]}:")
    for i, (currency, value) in enumerate(selectedYear.items()):
        print(f"{currency}: {(value * amount):.2f}{currencyOptions[i + 1][1]}")