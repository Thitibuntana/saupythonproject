myList = [10, 10, 10, "H", True, [20, 30, 40]]
myTuple = (10, 10, 10, "H", True, (20, 30, 40))
mySet = {10, 20, 10, "H", True, ("N","GG")}

testTuple = (1, 2, 3, 4, 5, 6, 7, {'SAU', 'DTI'})
print(min(list(testTuple[7])))
 
# Dictionary --->>>>>> Key : Value // key -> str-number // value -> anything
myDict = {"name":"nick", "age":20, 555:999, "flag":True}
print(myDict["age"], myDict[555])
print(myDict["name"])
myDict["major"] = "DTI"
myDict["name"] = "car"
print(myDict["name"])
print(myDict)
myDict.pop("name")
myDict.popitem()
print(myDict)

for i in myDict :
    print(i, end=" ")
print("")

for i in myDict.keys() :
    print(i, end=" ")
print("")

for i in myDict.values() :
    print(i, end=" ")
print("")

myDict1 = {"a":10, "b":20, "c":30}
myDict2 = myDict1
myDict3 = myDict1.copy
myDict1["a"] = 1
print(myDict1)
print(myDict2)
print(myDict3)