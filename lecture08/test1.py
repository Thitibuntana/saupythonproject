my_list = [10, 10, 10, "H", True, [20, 30, 40]]
my_tuple = (10, 10, 10, "H", True, (20, 30, 40))

# Set - has no order
my_set = {10, 20, 10, "H", True, ("N","GG")}

print(my_list)
print(my_tuple)
print(my_set)
print(len(my_list))
print(len(my_tuple))
print(len(my_set))

for i in my_set :
    print(i, end="/")
print("")
print('--------------------------')

list_fr_set = list(my_set)
list_fr_set[0] = 'DTI'
my_set = set(list_fr_set)
print(my_set)

mySet1 = {10, 20, 30, 'H'}
mySet2 = {10, "H", "B", True}

mySet1.add(999)
print(mySet1)
mySet1.remove("H")
print(mySet1)

print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))

# len, min, max
print(min(mySet1))
print(max(mySet1))
print(len(mySet1))

