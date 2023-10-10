#List/Tuple function
#len(), min(), max()

var1 = [10, 20, "Hello", True, [111, 'HUGE'], "biggie"]
var2 = (10, 20, "Hello", True, (111, 'HUGE'), "biggie")

print(f"there are {len(var1)} pieces of data in var1")
print(f"there are {len(var2)} pieces of data in var2")
# min/max cannot be used with different type of data.
var3 = [10, 20, 30, True, 10, 20]
var4 = (10, 20, 30, True, 10, 20)
print(min(var3))
print(max(var4))