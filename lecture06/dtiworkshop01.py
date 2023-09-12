def dataInput():
    return float(input("Insert base length: ")), float(input("Insert height: "))

def calcShow(base, height):
    areaValue = base * height * 1/2
    print(f"Triangle with base length of {base:.2f} and {height:.2f} tall would have area value of {areaValue:.2f}.")

print("-------------------------------")
print("--*Calculate Triangle Area*--")
print("-------------------------------")
base, height = dataInput()
print("-------------------------------")
calcShow(base, height)
print("-------------------------------")