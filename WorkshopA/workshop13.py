def inputValue():
    studentAmount = int(input("Student amount: "))
    return studentAmount

def calculateStuff(grade):
    textShow = "สอบไม่ผ่าน"
    if grade > 2:
        textShow = "สอบผ่าน"
    return textShow

def printStuff():
    print("**GRADE PASSING PROGRAM!!**")
    print("----------------------------------")
    studentAmount = inputValue()
    for i in range(1, studentAmount+1):
        stuName = input("Insert your name: ")
        stuID = input("Insert your ID: ")
        grade = float(input("Insert your grade: "))
        textShow = calculateStuff(grade)
        print(f"Student {stuID} {stuName} {textShow}")

printStuff()