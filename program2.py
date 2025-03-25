from AmountInPHP import AmountInPHP
from UserChoice import UserChoice

def Program2():
    platforms = ["PayPal", "GCash", "PayMaya", "Bank"]

    print("\n[--- [Digital Payment Platform Conversion] ---]\n")
    amount = AmountInPHP(Program2)
    if amount is None:
        return None

    print("Select a source platform:")
    for i in range(len(platforms)):
        print(f"{i + 1}. {platforms[i]}")
    print("5. Cancel\n")

    sourceChoice = UserChoice(5, Program2)
    if sourceChoice is None:
        return None
    print("[------------------------------------------------]\n")

    print("Select a target platform:")
    for i in range(len(platforms)):
        print(f"{i + 1}. {platforms[i]}")
    print("5. Cancel\n")

    targetChoice = UserChoice(5, Program2)
    if targetChoice is None:
        return None
    print("[------------------------------------------------]\n")
    
    source = platforms[sourceChoice - 1]
    target = platforms[targetChoice - 1]

    print((f"{source} to {target}\n").upper())

    converted = convertPHP(amount, source, target)
    print(f"Final converted amount: {converted:.2f} PHP")

def convertPHP(amount, source, target):
    # Transaction fee rates for different platforms
    fees = {
        "PayPal": 0.029,   # 2.9%
        "GCash": 0.02,     # 2.0%
        "PayMaya": 0.02,   # 2.0%
        "Bank": 0.015      # 1.5% Intra-bank transfers such as BDO to BDO, BPI to BPI etc.
    }
    
    isSamePlatform = source == target
    
    feeRate = 0.0 if isSamePlatform else fees[target]
    feeAmount = amount * feeRate
    totalAmount = amount + feeAmount
    if isSamePlatform:
        print(f"There is no charge :)")
    else:
        print(f"The transaction fee for {source} is {(fees[source] * 100):.1f}%, so the fee is {feeAmount:.2f} PHP: {amount:.2f} + {feeAmount:.2f} PHP")
    
    return totalAmount
