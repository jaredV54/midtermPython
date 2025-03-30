# Our sources:
# https://www.exchange-rates.org
# https://v6.exchangerate-api.com

import requests

def GetExchangeRate():
    url = "https://v6.exchangerate-api.com/v6/d9c62ee20a9ce6083497c9c1/latest/PHP"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        if data['result'] == 'success':
            conversionRates = data['conversion_rates']
            return {
                "USD": conversionRates.get("USD"),
                "AUD": conversionRates.get("AUD"),
                "JPY": conversionRates.get("JPY"),
                "KRW": conversionRates.get("KRW")
            }
            
    except requests.exceptions.RequestException:
        print(f"\nNetwork error occurred!!! \nUsing historical exchange rates as of March 25, 2025.")
        return {
            "USD": 0.01747,  
            "AUD": 0.02775,  
            "KRW": 25.6011,
            "JPY": 2.5973
        }

def GetExchangeRatePerYear():
    # Limited 2021-2024
    # We displayed the average exchange rates
    return {
        "2021": {
            "USD": 0.02030,
            "AUD": 0.02703,
            "KRW": 23.230,
            "JPY": 2.2290
        },
        "2022": {
            "USD": 0.01838,
            "AUD": 0.02646,
            "KRW": 23.689,
            "JPY": 2.4099
        },
        "2023": {
            "USD": 0.01798,
            "AUD": 0.02707,
            "KRW": 23.469,
            "JPY": 2.5253
        },
        "2024": {
            "USD": 0.01746,
            "AUD": 0.02646,
            "KRW": 23.786,
            "JPY": 2.4876
        },
    }

def GetCurrencyOptions():
    return {
        1: ("USD", "$", [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]),
        2: ("AUD", "$", [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 0.50, 0.20, 0.10, 0.05]),
        3: ("KRW", "₩", [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]),
        4: ("JPY", "¥", [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1])
    }

def GetCryptoCurrencies(targetPhysical, targetCrypto, amount):
    url = f"https://api.fastforex.io/convert?from={targetPhysical}&to={targetCrypto}&amount={amount}&precision=2&api_key=ba8f9e999c-19a302c8ad-strv72"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.json()
        
    except requests.exceptions.RequestException:
        return None
