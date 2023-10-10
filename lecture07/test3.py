# List method
var1 = [10, 20, "Hello", True, [111, 'HUGE'], "biggie"]
var2 = (10, 20, "Hello", True, (111, 'HUGE'), "biggie")

#append
var1.append(555)
var1.append(["Hi", "Hey", 999])
print(var1)
#extend
var1.extend([10, 20, 30])
print(var1)
#remove
var1.remove("Hello")
var1.remove(10)
print(var1)
#---------------------
var2 = [10, 20, "Hello"]
#insert
var2.insert(2, "Hi")
print(var2)
#pop
var2.pop(1)
print(var2)
#index
print(var2.index("Hi"))
#count
print(var1.count(10))
#-------------------------
var3 = [10, 10, 10, 10, 20, "Epic"]
print(f"var3 has {var3.count(10)} ten(s)")
print(f"var3 has {var3.count('Epic')} \"Epic\"")
#-------------------------
var4 = [10, 11, 34543, 32, 20]
var5 = ["C", "CO", "CA", "COO", "COOL"]
#sort
#needs to be the same type of data
var4.sort()
var5.sort()
print(var4)
print(var5)
var5.sort(reverse=True)
print(var5)

