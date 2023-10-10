# Tuple to List, vice versa

var2 = (10, 20, "Hello", True, (111, 'HUGE'), "biggie")

#list(), tuple()

varTemp = list(var2)
varTemp[2] = "Hi"
var2 = tuple(varTemp)
print(var2)