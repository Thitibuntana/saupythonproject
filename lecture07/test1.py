#variable
score = 5456
stu_name = "big man"
flag = True
# -----------------
#List
    #   0   1   2          3    4               5
var1 = [10, 20, "Hello", True, [111, 'HUGE'], "biggie"]
    #   -6  -5  -4         -3   -2              -1

print(var1[0] + var1[1])
print(var1[0] + var1[4][0])

#Tuple
    #   0   1   2          3    4               5
var2 = (10, 20, "Hello", True, (111, 'HUGE'), "biggie")
    #   -6  -5  -4         -3   -2              -1

print(var2[0] + var2[-5])
print(f"{var2[2]}...{var1[5]}")


