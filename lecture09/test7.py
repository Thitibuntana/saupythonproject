import test6
import math
from test8 import calSquareArea, calCircleArea, calTriArea

print(f"10 + 20 = {test6.sumNumber(10, 20)}")

test6.showHi()

print(f"VAT for 20,000$ product is {20000 * test6.VAT}$")

print(f"7^15 = {math.pow(7, 15)}")

print(f"Area of circle with radius of 3: {math.pi * math.pow(3, 2)}")

print(f"4 by 4 Square area: {calSquareArea(4, 4)}")
print(f"Area of circle with radius of 5 {calCircleArea(5)}")
print(f"Triangle with 3 cm base and is 4 cm tall's area: {calTriArea(3, 4)}")

