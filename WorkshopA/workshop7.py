def inputValue():
    luckyNumber = int(input("YOUR LUCKY NUMBER!: "))
    return luckyNumber

def calculateStuff(value):
    realNumber = 25
    textShow = "Not Correct !!!."
    if value == realNumber:
        textShow = "Correct, You are the winner"
    return textShow

def printStuff():
    print("**BINGO GAME!! GUESS THE NUMBER!!**")
    luckyNumber = inputValue()
    textShow = calculateStuff(luckyNumber)
    print(textShow)

printStuff()