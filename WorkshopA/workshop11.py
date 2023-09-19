def inputValue():
    phoneUser = input("Phone user: ")
    phoneNumber = input("Phone number: ")
    phoneMinute = float(input("Usage duration (Minute): "))
    return phoneUser, phoneNumber, phoneMinute

def calculateStuff(minute):
    pricePerMinute = 0
    if minute < 1:
        pricePerMinute = 0
    elif minute < 16:
        pricePerMinute = 5
    elif minute < 31:
        pricePerMinute = 3
    else:
        pricePerMinute = 1.5
    return minute * pricePerMinute

def printStuff():
    print("**TELEPHONE PAYMENT CALCULATOR**")
    print("----------------------------------")
    phoneUser, phoneNumber, phoneMinute = inputValue()
    callPrice = calculateStuff(phoneMinute)
    roundedCallPrice = format(callPrice, ".2f")
    print(f"{phoneUser}, PHONE NUMBER {phoneNumber} CALLED FOR {phoneMinute}, PAYMENT: {roundedCallPrice} BAHT.")

printStuff()