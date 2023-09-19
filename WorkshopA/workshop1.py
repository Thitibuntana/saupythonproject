def inputItemData():
    itemName = input("Name of the product: ")
    itemBudget = float(input("Base value: "))
    return itemName, itemBudget

def calculateStuff(budget):
    return budget + (budget * 1/10)

def printStuff():
    itemName, itemBudget = inputItemData()
    itemBudget = calculateStuff(itemBudget)
    roundedPrice = format(itemBudget, ".2f")
    print(f"The price of {itemName} would be {roundedPrice} Baht.")

printStuff()