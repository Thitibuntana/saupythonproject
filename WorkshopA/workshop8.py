def inputValue():
    provinceName = input("Province: ")
    waterPH = float(input("Water's PH value: "))
    return provinceName, waterPH

def calculateStuff(value):
    textShow = "Result is Normal"
    if value > 8:
        textShow = "Result is Acid"
    elif value < 7:
        textShow = "Result is Alkali"
    return textShow

def printStuff():
    print("**Water status checker!!!**")
    provinceName, waterPH = inputValue()
    textShow = calculateStuff(waterPH)
    print(f"THE PROVINCE {provinceName}'s WATER STATUS: {textShow}")

printStuff()