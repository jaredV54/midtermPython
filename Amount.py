def AmountInPhysicalCurrency(currency):
    while True:
        try:
            if currency in ["PHP", "USD", "AUD"]:
                amount = float(input(f"Enter the amount in {currency}: "))
            else:
                amount = int(input(f"Enter the amount in {currency}: "))

            if amount <= 0:
                print("Amount must be a positive number.")
                continue

        except ValueError:
            if currency not in ["PHP", "USD", "AUD"]:
                print("Invalid amount. Please enter a whole number for non-PHP/USD/AUD currencies.")
            else:
                print("Invalid amount. Please enter a valid monetary value.")
            continue

        return amount