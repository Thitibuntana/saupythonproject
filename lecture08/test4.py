class Test04 :
    data1 = 10
    

    def __init__(self, x=2, y=5):
        print("Hi...")
        self.data2 = x
        self.data3 = y

    def showSumData(self):
        print(self.data1 + self.data2 + self.data3)

    def showWow(self): 
        print("WWWWWWWWWWWWWWW")


objA = Test04(25,50)
objB = Test04(15,60)
objC = Test04(45,100)
objD = Test04(125,250)
print(objA.data2)