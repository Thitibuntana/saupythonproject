class DTITest03 :
    infoA = 12

    def __init__(self, infoB = 1, infoC = 1):
        self.infoB = infoB
        self.infoC = infoC

    def showMixAndInfo(self, mix=2) :
        print(f"{self.infoA} + {self.infoB} + {self.infoC} + {mix} = {self.infoA + self.infoB + self.infoC + mix}")

objA = DTITest03(2, 4)
objA.showMixAndInfo(6)