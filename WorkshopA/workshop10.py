def inputValue():
    studentYear = int(input("Insert your student year (1, 2, 3, 4): "))
    return studentYear

def calculateStuff(value):
    textShow = "Welcome Freshman"
    if value == 1:
        textShow = "Welcome Freshman"
    elif value == 2:
        textShow = "Welcome Sophomore"
    elif value == 3:
        textShow = "Welcome Junior"
    else:
        textShow = "Welcome Senior"
    return textShow

def printStuff():
    print("**WELCOME STUDENT!!**")
    print("----------------------------------")
    studentYear = inputValue()
    textShow = calculateStuff(studentYear)
    print(textShow)

printStuff()