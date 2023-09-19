def inputValue():
    tourHead = input("Phone user: ")
    headPhoneNumber = input("Phone number: ")
    peopleAmount = int(input("Usage duration (Minute): "))
    return tourHead, headPhoneNumber, peopleAmount

def calculateStuff(people):
    packagePrice = 300
    if people < 3:
        packagePrice = 300
    elif people < 6:
        packagePrice = 250
    elif people < 11:
        packagePrice = 210
    else:
        packagePrice = 150
    return people * packagePrice, packagePrice

def printStuff():
    print("**TOUR PACKAGE PRICE CALCULATION**")
    print("----------------------------------")
    tourHead, headPhoneNumber, peopleAmount = inputValue()
    totalPrice, pricePerPackage = calculateStuff(peopleAmount)
    roundedtotalPrice = format(totalPrice, ".2f")
    print(f"TOUR HEAD: {tourHead}, PHONE NUMBER: {headPhoneNumber} AMOUNT OF PEOPLE: {peopleAmount} // PRICE PER PACKAGE: {pricePerPackage} BAHT. TOTAL PRICE: {totalPrice} BAHT.")

printStuff()