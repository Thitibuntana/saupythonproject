empId = input("Employee ID: ")
empName = input("Employee Name: ")
empSalary = float(input("Salary (Baht): "))

taxAmount = 7/100
socialSecurity = 500

def getFinalSalary(theSalary) :
    finalSalary = theSalary - ((theSalary * taxAmount) - socialSecurity)
    return format(finalSalary, ".2f")

print(f"""
    ----------------------------------------
    EMPLOYEE ID: {empId}
    EMPLOYEE NAME: {empName}
    CALCULATED SALARY: {getFinalSalary(empSalary)} BAHT
    ----------------------------------------
""")
