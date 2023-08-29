productName = input("Insert the name of the product: ")
initialPrice = float(input("Insert initial price (Baht): "))

def getPrice(budget) :
    tempPrice = budget + (budget*(1/10))
    return format(tempPrice, ".2f")

print(f"The sell price for {productName} is {getPrice(initialPrice)} Baht.")