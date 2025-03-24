def AmountInPHP(callbackFunc = None):
    try:
        amount = float(input("Enter the amount in PHP: "))
        if amount <= 0:
            print("Amount must be a positive number.")
            callbackFunc()
            return None
    except ValueError:
        print("Invalid amount. Please enter a cash amount in number.")
        callbackFunc()
        return None
    return amount