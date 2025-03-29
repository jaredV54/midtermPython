import requests
from UserChoice import UserChoice
from AmountInPHP import AmountInPHP

def fetchCryptoPrices(targetCrypto, amount):
    url = f"https://api.fastforex.io/convert?from=PHP&to={targetCrypto}&amount={amount}&precision=2&api_key=ba8f9e999c-19a302c8ad-strv72"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()

        if "result" in data:
            return data["result"]
    except requests.exceptions.RequestException:
        return None

def Program3():
    while True:
        print("\n[--------- [ Forex Exchange Conversion ] ---------]\n")
        cryptoCurrencies = ["BTC", "SOL", "XRP", "ETH"]

        print("Select a crypto currency:")
        for i in range(1, 5):
            print(f"{i}. {cryptoCurrencies[i - 1]}")
        print(f"5. Cancel\n")

        choice = UserChoice(5)
        if choice == "break":
            break
        elif choice == "continue":
            continue

        amount = AmountInPHP()
        if amount == "continue":
            continue

        targetCrypto = cryptoCurrencies[choice - 1]

        print("\n[--------------- [ Processing... ]---------------]\n")

        prices = fetchCryptoPrices(targetCrypto, amount)
        if not prices:
            print("Network error occurred!!! Please try again.")
            print("Please make sure you are connected to the internet.")
            continue
        
        print(f"PHP: {amount}")
        print(f"{targetCrypto}: {prices[targetCrypto]}")
        print(f"Rate: {prices["rate"]}")
        break
        