class DTITest04:
    data1 = 1

    def __init__(self, data2=5, data3=15) :
        self.data2 = data2
        self.data3 = data3
        print("Creating object.")

    def Task1(self):
        print("^_^'")

    def Task2(self, v):
        print(v)

    def __del__(self):
        print("Bye!")

objA = DTITest04()
objB = DTITest04(10,20)
objC = DTITest04(15)
 
objC.Task2("T_T")
objC.Task1()
print(f"objA.data1 + objB.data1 = {objA.data1 + objB.data1}")