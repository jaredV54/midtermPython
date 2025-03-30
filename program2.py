from Amount import AmountInPhysicalCurrency
from UserChoice import UserChoice

def Program2():
    while True:
        PLATFORMS = ["PayPal", "GCash", "PayMaya", "Bank"]

        print("\n[--- [PHP Digital Payment Platform Conversion] ---]\n")
        amount = AmountInPhysicalCurrency("PHP")

        print("\nSelect a source platform:")
        for i in range(len(PLATFORMS)):
            print(f"{i + 1}. {PLATFORMS[i]}")
        print("5. Cancel\n")

        sourceChoice = UserChoice(5)
        if sourceChoice == "break":
            break
        print("\n[------------------------------------------------]\n")

        print("Select a target platform:")
        for i in range(len(PLATFORMS)):
            print(f"{i + 1}. {PLATFORMS[i]}")
        print("5. Cancel\n")

        targetChoice = UserChoice(5)
        if targetChoice == "break":
            break
        print("\n[------------------------------------------------]\n")
        
        source = PLATFORMS[sourceChoice - 1]
        target = PLATFORMS[targetChoice - 1]

        print((f"{source} to {target}\n").upper())

        converted = convertToDigitalPlatform(amount, source, target)
        print(f"Amount to pay: {converted:.2f}₱")
        print(f"Amount they receive: {amount:.2f}₱")
        
        break  

def convertToDigitalPlatform(amount, source, target):
    # Transaction fee rates for different PLATFORMS
    fees = {
        "PayPal": 0.029,   
        "GCash": 0.02,     
        "PayMaya": 0.02,   
        "Bank": 0.015      # Like Intra-bank transfers such as BDO to BDO, BPI to BPI etc.
    }
    
    isSamePlatform = source == target
    
    feeRate = 0.0 if isSamePlatform else fees[target]
    feeAmount = amount * feeRate
    totalAmount = amount + feeAmount
    if isSamePlatform:
        print(f"There is no charge :)")
    else:
        print(f"Transaction fee for {source}: {(fees[source] * 100):.1f}%")
        print(f"PHP: {amount:.2f}₱")
        print(f"Fee: {feeAmount:.2f}₱\n")
    
    return totalAmount
