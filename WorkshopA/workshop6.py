def inputValue():
    debtorName = input("Debtor's name: ")
    loanValue = float(input("Loan amount: "))
    return debtorName, loanValue

def calculateStuff(value):
    rate = 2.5/100
    if value < 1000:
        rate = 5.5/100
    else:
        rate = 2.5/100
    interest = value * rate
    return interest

def printStuff():
    debtorName, loanValue = inputValue()
    interest = calculateStuff(loanValue)
    print(f"DEBTOR {debtorName} WITH THE LOAN OF {loanValue} WOULD HAVE AN INTEREST OF {interest} BAHT.")

printStuff()