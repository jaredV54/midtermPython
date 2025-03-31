# Our sources for exchange rates:
# https://www.exchange-rates.org
# https://v6.exchangerate-api.com

import requests  # Import the requests library to make HTTP requests

def GetExchangeRate():
    # URL to get the latest exchange rates for PHP
    url = "https://v6.exchangerate-api.com/v6/d9c62ee20a9ce6083497c9c1/latest/PHP"
    
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        # Raise an error if the request was unsuccessful
        response.raise_for_status() 
        # Convert the response to JSON format
        data = response.json()

        # Check if the API call was successful
        if data['result'] == 'success':
            # Get the conversion rates from the data
            conversionRates = data['conversion_rates']
            # Return the conversion rates for specific currencies
            return {
                "USD": conversionRates.get("USD"),
                "AUD": conversionRates.get("AUD"),
                "JPY": conversionRates.get("JPY"),
                "KRW": conversionRates.get("KRW")
            }
            
    except requests.exceptions.RequestException:
        # Print an error message if a network error occurs
        print(f"\nNetwork error occurred!!! \nUsing historical exchange rates as of March 25, 2025.")
        # Return historical exchange rates if there's a network error
        return {
            "USD": 0.01747,  
            "AUD": 0.02775,  
            "KRW": 25.6011,
            "JPY": 2.5973
        }

def GetExchangeRatePerYear():
    # Provide average exchange rates for the years 2021 to 2024
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
    # Provide currency options with denominations for each currency
    return {
        1: ("USD", "$", [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]),
        2: ("AUD", "$", [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 0.50, 0.20, 0.10, 0.05]),
        3: ("KRW", "₩", [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]),
        4: ("JPY", "¥", [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1])
    }

def GetCryptoCurrencies(targetPhysical, targetCrypto, amount):
    # URL to convert physical currency to cryptocurrency
    url = f"https://api.fastforex.io/convert?from={targetPhysical}&to={targetCrypto}&amount={amount}&precision=2&api_key=ba8f9e999c-19a302c8ad-strv72"
    headers = {"accept": "application/json"}

    try:
        # Make a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()  
        # Return the response in JSON format
        return response.json()
        
    except requests.exceptions.RequestException:
        # Print an error message if a network error occurs
        print("Network error occurred!!! Please try again.")
        print("Please make sure you are connected to the internet.")
        # Return None if there's a network error
        return None