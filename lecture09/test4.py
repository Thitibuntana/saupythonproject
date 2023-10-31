class DTITest05 :
    infoA = 10
    __infoB = 20

    def __init__(self, infoC=0, infoD=0):
        self.infoC = infoC
        self.__infoD = infoD



    def setInfoB(self, infoB):
        self.__infoB = infoB

    def getInfoB(self):
        return self.__infoB
    
    def setInfoD(self, infoD):
        self.__infoD = infoD

    def getInfoD(self):
        return self.__infoD
    
    def showInfo(self):
        print(self.infoA, end=" ")
        print(self.__infoB, end=" ")
        print(self.infoC, end=" ")
        print(self.__infoD, end=" ")
        print("")


obj1 = DTITest05(30,40)
obj2 = DTITest05(20,140)

obj1.showInfo()
obj1.__infoB = 999 # -- does nothing
obj1.setInfoB(998)
obj1.showInfo()
print(obj1.getInfoD() + obj1.getInfoB())
