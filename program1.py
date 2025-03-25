from Currency import GetExchangeRate, GetCurrencyOptions
from UserChoice import UserChoice
from AmountInPHP import AmountInPHP

def Program1():
    exchangeRates = GetExchangeRate()
    currencyOptions = GetCurrencyOptions()

    print("\n[---------- [ Currency Exchange Menu ] ----------]\n")
    for i, (code, symbol, _) in currencyOptions.items():
        print(f"{i}. {code} ({symbol})")
    print("5. Cancel\n")

    choice = UserChoice(5, Program1)
    if choice is None:
        return None
    
    amount = AmountInPHP(Program1)
    if amount is None:
        return None
    
    print("\n[------------------------------------------------]\n")
   
    currencyCode, symbol, denominations = currencyOptions[choice]
    converted = amount * exchangeRates[currencyCode]

    smallestDenomination = min(denominations)
    converted = round(converted / smallestDenomination) * smallestDenomination

    print(f"Converted amount: {symbol}{converted:.2f} {currencyCode}")

    breakdown = breakdownAmount(converted, denominations)
    print("\nBreakdown:")
    for denom, count in breakdown.items():
            print(f"{count} x {int(denom * 100)}¢" if currencyCode in ["USD", "AUD"] else f"{count} x {symbol}{denom} {currencyCode}")
    
def breakdownAmount(amount, denominations):
    breakdown = {}
    remaining = amount
    for denom in denominations:
        count = int(remaining // denom)
        if count > 0:
            breakdown[denom] = count
            remaining = round(remaining - denom * count, 2) 
    return breakdown