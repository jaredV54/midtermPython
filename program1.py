from Currency import GetExchangeRate, GetCurrencyOptions
from UserChoice import UserChoice
from Amount import AmountInPhysicalCurrency

def Program1():
    while True:
        currencyOptions = GetCurrencyOptions()

        print("\n[-------- [ PHP Currency Exchange Menu ] --------]\n")
        for i in range(1, 5):
            code, symbol, _ = currencyOptions[i]
            print(f"{i}. {code} ({symbol})")
        print("5. Cancel\n")
 
        choice = UserChoice(5)
        if choice == "break":
            break
        
        amount = AmountInPhysicalCurrency("PHP")
        print("\n[--------------- [ Processing... ]---------------]\n")

        exchangeRates = GetExchangeRate()
        currencyCode, symbol, denominations = currencyOptions[choice]
        converted = amount * exchangeRates[currencyCode]

        smallestDenomination = min(denominations)
        converted = round(converted / smallestDenomination) * smallestDenomination

        print("Converted amount:", end=" ")
        print(f"{symbol}{converted:.2f}" if currencyCode in ['USD', 'AUD'] else f"{symbol}{converted} {currencyCode}")

        breakdown = breakdownAmount(converted, denominations)
        print("\nBreakdown:")
        for denom in breakdown:
            count = breakdown[denom]
            if currencyCode in ["USD", "AUD"]:
                print(f"{count} x " + f"{int(denom * 100)}¢" if denom < 1 else f"{count} x {denom}$")
            else:
                print(f"{count} x {symbol}{denom}")
        
        break  
            
def breakdownAmount(amount, denominations):
    breakdown = {}
    remaining = amount

    for denom in denominations:
        count = int(remaining // denom)
        if count > 0:
            breakdown[denom] = count
            remaining = round(remaining - denom * count, 2) 
    return breakdown
