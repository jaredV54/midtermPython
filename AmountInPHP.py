def AmountInPHP():
    try:
        amount = float(input("Enter the amount in PHP: "))
        if amount <= 0:
            print("Amount must be a positive number.")
            return 'continue'
    except ValueError:
        print("Invalid amount. Please enter a cash amount in number.")
        return 'continue'
    return amount
