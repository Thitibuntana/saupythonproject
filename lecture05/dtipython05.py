def getValue():
    people = round(int(input("Amount of people: ")))
    money = float(input("Amount of money: "))
    return people, money

initialPeople, initialMoney = getValue()

def averageMoneyPrint(people, money):
    averageMoney = money/people
    formattedMoney = format(money, ".2f")
    roundedMoney = round(averageMoney)
    print(f"""
        People amount: {people}
        Money amount: {formattedMoney}
        Average per person would be: {roundedMoney}
    """)
    print("There are {0} people and {1} Baht, so the share would be {2} per person.".format(people, formattedMoney, roundedMoney))
    print("There are " + str(people) + " people and " + str(formattedMoney) + " Baht, so the share would be " + str(roundedMoney) + " per person.")
    print("There are", people, "people and", formattedMoney, "Baht, so the share would be", roundedMoney, "per person.")
    print("There are %i people and %s Baht, so the share would be %i per person." % (people, formattedMoney, roundedMoney))

averageMoneyPrint(initialPeople, initialMoney)