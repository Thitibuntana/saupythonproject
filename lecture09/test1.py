class DTITest01 :
    pass

class DTITest02 :
    infoA = ""
    infoB = 20

    def showHi(self) :
        print("Hi")

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)


objA = DTITest02()
objB = DTITest02()
objC = DTITest02()
objA.infoA = "INFO A"
objB.infoB = 200
objA.showInfoAandB()
print(f"objA.infoB + objB.infoB = {objA.infoB + objB.infoB}")

