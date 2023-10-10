# Slicing data in List and Tuple

var1 = [10, 20, "Hello", True, [111, 'HUGE'], "biggie"]

var2 = (10, 20, "Hello", True, (111, 'HUGE'), "biggie")

# 20, "Hello", True
print(var1[1:4])
# True, (111, 'HUGE')
print(var2[3:5])
# 10, 20, "Hello"
print(var1[:3])
# "Hello", True, [111, 'HUGE'], "biggie"
print(var2[:2])



