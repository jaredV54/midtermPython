def AmountInPhysicalCurrency(currency):
    # This function prompts the user to enter an amount in a specified currency
    # It ensures that the input is valid and positive before returning it

    while True:
        # This loop will continue until the user provides a valid input
        try:
            # Check if the currency is one of the specified types that allow decimal values
            if currency in ["PHP", "USD", "AUD"]:
                # Prompt the user to enter a monetary amount, allowing for decimals
                amount = float(input(f"Enter the amount in {currency}: "))
            else:
                # For other currencies, prompt the user to enter a whole number
                amount = int(input(f"Enter the amount in {currency}: "))

            # Check if the entered amount is positive
            if amount <= 0:
                # If not, print an error message and prompt again
                print("Amount must be a positive number.")
                continue

        except ValueError:
            # If the user enters an invalid value (non-numeric), catch the error
            if currency not in ["PHP", "USD", "AUD"]:
                # For non-decimal currencies, print a specific error message
                print("Invalid amount. Please enter a whole number for non-PHP/USD/AUD currencies.")
            else:
                # For decimal currencies, print a general error message
                print("Invalid amount. Please enter a valid monetary value.")
            # Continue the loop to prompt the user again
            continue

        # If the input is valid and positive, return the amount
        return amount