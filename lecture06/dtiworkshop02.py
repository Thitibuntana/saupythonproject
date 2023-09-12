def truckDefiner() :
    registration = input("Car registration: ")
    weight = float(input("Overall weight (KG): "))
    return registration, weight

def passingTruck(registration, weight):
    if weight <= 1000 :
        print(f"รถทะเบียน {registration} ผ่านเกณฑ์ ({weight:.2f} KG)")
    else:
        print(f"รถทะเบียน {registration} ไม่ผ่านเกณฑ์ ({weight} KG)")

print("-------------------------------")
print("--*Truck Checker*--") # truck checker gimme the truck checker yeahhh the truck checker i knew you could do it
print("-------------------------------")
registration, weight = truckDefiner()
print("-------------------------------")
passingTruck(registration, weight)
print("-------------------------------")