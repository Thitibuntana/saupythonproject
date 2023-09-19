def inputItemData():
    itemName = input("Name of the product: ")
    itemBudget = float(input("Price: "))
    return itemName, itemBudget

def calculateStuff(budget):
    return budget * 7/100

def printStuff():
    itemName, itemBudget = inputItemData()
    itemTax = calculateStuff(itemBudget)
    roundedTax = format(itemBudget, ".2f")
    roundedPrice = format(itemBudget, ".2f")
    print(f"The product {itemName} sold at {roundedPrice} Baht would have VAT of {roundedTax} Baht.")

printStuff()