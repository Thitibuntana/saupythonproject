moneyInput = input("Insert the amount of money: ")
amountOfPeople = input("Insert the amount of people: ")
productValue = int(moneyInput)/float(amountOfPeople)
productValueText = format(productValue, ".2f")
print("By average, you would get", productValueText, "Baht per person.")
print("By average, you would get " + productValueText + " Baht per person.")
print("By average, you would get {} Baht per person.".format(productValueText))
print(f"By average, you would get {productValueText} Baht per person.")
