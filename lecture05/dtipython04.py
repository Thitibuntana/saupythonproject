#Function 4: have parameters / have returns

def getMath(n1, n2):
    return n1 + n2, n1 - n2

def mathPower(n1 ,n2):
    print(f"{n1} ^ {n2} = {n1 ** n2}")
    return n1 ** n2

poweredMoney = mathPower(2 , 12.25)
money, tax = getMath(poweredMoney , 193.25)
print(format(money, ".2f"), format(tax, ".2f"))