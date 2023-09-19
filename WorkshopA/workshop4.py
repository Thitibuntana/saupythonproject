def inputX():
    valueX = float(input("Insert the value of X: "))
    return valueX

def calculateStuff(x):
    valueY = (2*(x**2)) + (2*x) + 1
    return valueY

def printStuff():
    valueX = inputX()
    valueY = calculateStuff(valueX)
    print(f"If you replace x in y = 2x^2 + 2x + 1 with {valueX}, you would get Y as {valueY}")

printStuff()