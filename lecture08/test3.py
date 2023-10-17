# OOP
class DtiSau :
    # data/property member
    stuName = ''
    score = 0
    gpa = 0

    # method member
    def hiStudent(self) :
        print(f'Hello {self.stuName}')
    def showScoreAndGrade(self) :
        print(f'Score: {self.score} | GPA: {self.gpa}')

obj1 = DtiSau()
obj2 = DtiSau()

obj1.stuName = "Nick"
obj1.score = 99
obj1.gpa = "A"
obj1.hiStudent()
obj1.showScoreAndGrade()

    