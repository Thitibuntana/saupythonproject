class SAU1 :
    infoA = 10

    def showHi():
        print("Hi")

class SAU2(SAU1):
    infoB = 20

    def showHey():
        print("Hey")

obj1 = SAU2()
obj1.showHi()