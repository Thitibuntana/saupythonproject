def inputEmpData():
    empName = input("Employee name: ")
    empID = input("Employee Id: ")
    empSalary = float(input("Salary: "))
    return empName, empID, empSalary

def getFinalSalary(salary):
    finalSalary = salary - (salary*7/100) - 500
    return finalSalary

def printStuff():
    print("**NET SALARY CALCULATOR**")
    print("----------------------------------")
    empName, empID, empSalary = inputEmpData()
    finalSalary = getFinalSalary(empSalary)
    roundedSalary = format(finalSalary, ".2f")
    print(f"EMPLOYEE {empName} ID {empID} WITH SALARY OF {empSalary} WOULD HAVE NET SALARY OF {roundedSalary} BAHT.")

printStuff()