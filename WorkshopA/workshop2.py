def inputName():
    stuName = input("Student name: ")
    stuID = input("Student Id: ")
    return stuName, stuID

def getScore():
    return float(input("Insert first time's score: ")), float(input("Insert second time's score: ")), float(input("Insert third time's score: "))

def printStuff():
    stuName, stuID = inputName()
    score1, score2, score3 = getScore()
    averageScore = (score1+score2+score3)/3
    roundedScore = format(averageScore, ".2f")
    print(f"The average score of student {stuName} ID {stuID} would be {roundedScore} point(s).")

printStuff()