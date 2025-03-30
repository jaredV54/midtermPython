from UserChoice import UserChoice
from Amount import AmountInPhysicalCurrency
from Currency import GetCryptoCurrencies

def Program3():
    while True:
        print("\n[--------- [ Forex Exchange Conversion ] ---------]\n")

        PHYSICAL_CURRENCIES = ["PHP","USD", "AUD", "KRW", "JPY"]
        CRYPTO_CURRENCIES = ["BTC", "SOL", "XRP", "ETH"]

        print("Select a Physical Currency:")
        for i in range(1, 6):
            print(f"{i}. {PHYSICAL_CURRENCIES[i - 1]}")
        print(f"6. Cancel\n")

        physicalCurrency = UserChoice(6)
        if physicalCurrency == "break":
            break

        print("\nSelect a Crypto Currency:")
        for i in range(1, 5):
            print(f"{i}. {CRYPTO_CURRENCIES[i - 1]}")
        print(f"5. Cancel\n")

        crytoCurrency = UserChoice(5)
        if crytoCurrency == "break":
            break

        source = PHYSICAL_CURRENCIES[physicalCurrency - 1]
        target = CRYPTO_CURRENCIES[crytoCurrency - 1]
        amount = AmountInPhysicalCurrency(source)

        print("\n[--------------- [ Processing... ]---------------]\n")

        prices = GetCryptoCurrencies(source, target, amount)
        if not prices:
            continue
        
        print(f"{source}: {prices["amount"]}")
        print(f"{target}: {prices["result"][target]}")
        print(f"Rate: {prices["result"]["rate"]}")
        break