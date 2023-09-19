def inputEmpData():
    empName = input("Employee name: ")
    empID = input("Employee Id: ")
    empSales = float(input("Sales: "))
    return empName, empID, empSales

def calculateComm(sales):
    commissionRate = 0
    if sales < 1001:
        commissionRate = 0
    elif sales < 2001:
        commissionRate = 1/100
    elif sales < 3001:
        commissionRate = 3/100
    else:
        commissionRate = 5/100
    commission = sales * commissionRate
    return commission

def printStuff():
    print("**COMMISSION CALCULATOR**")
    print("----------------------------------")
    empName, empID, empSales = inputEmpData()
    commission = calculateComm(empSales)
    roundedCommission = format(commission, ".2f")
    print(f"EMPLOYEE {empName} ID {empID} WITH SALES OF {empSales} WOULD GET COMMISSION OF {roundedCommission} BAHT.")

printStuff()