from Currency import GetExchangeRate, GetCurrencyOptions
from UserChoice import UserChoice
from AmountInPHP import AmountInPHP

def Program1():
    exchangeRates = GetExchangeRate()
    currencyOptions = GetCurrencyOptions()

    print("\n[---------- [ Currency Exchange Menu ] ----------]\n")
    for i in range(1, len(currencyOptions) + 1):
        code, symbol, _ = currencyOptions[i]
        print(f"{i}. {code} ({symbol})")
    print(f"{len(currencyOptions) + 1}. Cancel\n")

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
    for denom in breakdown:
        count = breakdown[denom]
        if currencyCode in ["USD", "AUD"]:
            print(f"{count} x {int(denom * 100)}¢")
        else:
            print(f"{count} x {symbol}{denom} {currencyCode}")
            
def breakdownAmount(amount, denominations):
    breakdown = {}
    remaining = amount
    for denom in denominations:
        count = int(remaining // denom)
        if count > 0:
            breakdown[denom] = count
            remaining = round(remaining - denom * count, 2) 
    return breakdown