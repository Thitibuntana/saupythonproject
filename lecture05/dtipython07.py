#built-in function
import math

def getValue():
    return float(input("Insert the radius: "))

def calcArea(radius):
    return math.pi * (radius**2)

def calcCircumference(radius):
    return 2*(math.pi*radius)

def clacVolume(radius):
    return 4/3 * math.pi * (radius**3)

def showCalc():
    radius = getValue()
    area = calcArea(radius)
    circ = calcCircumference(radius)
    vol = clacVolume(radius)
    print(f"""
        Sphere radius: {"%.4f"%radius}
        Area: {"%.4f"%area}
        Circumference: {"%.4f"%circ}
        Volume: {"%.4f"%vol}
          """)
    
showCalc()

    
    