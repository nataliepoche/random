# List comprehension, one line statements
# Non list
cashier_3 = []
for item in cart:
    if item % 2 == 0:
        cashier_3.append(item)

# list comprehension
cashier_3 = [item for item in cart if item % 2 == 0]

# List for 1-100, accepts all even integers
print("List 1-100, even integers")
list = [item for item in range(1,101) if item % 2 == 0]
print(list)

# List 1-100, both even and odd
print("List 1-100 both even and odd")
list = [item for item in range(1,101)]
print(list)

# List 1-10
list = [item for item in range(1,11)]
print(list)

# Shallow lists
# Connected lists, used normal
mylist = [1, 2, 3]
shallowcopy = mylist

print(mylist, shallowcopy)

mylist[0] = 9

print(mylist, shallowcopy) # Changes the value over to mylist, this is bc when assign those two lists, they share the same memory space\

# Deep list
# Copy and original doesn't have the same values
mylist = [1, 2, 3]
shallowcopy = mylist[:] # Ensures that the lists aren't conencted

print(mylist, shallowcopy)

mylist[0] = 9

print(mylist, shallowcopy)

# Create a list [1, 2, 3, 4, 5]
mylist = [1, 2, 3, 4, 5]
# Create a deep copy, change the first value to -3
deepcopy = mylist[:]
deepcopy[0] = -3
# print both lists
print(mylist, deepcopy)

# Create a shallow copy of the list
shallowcopy = mylist
# create a shallow copy, change the first value to -3
shallowcopy[0] = -3
mylist[0] = 99
# print both lists
print(mylist, shallowcopy)

# Tuple, secures list values from change ()
mytupple = (1,2,3,4,5)
mytupple[0] = 99
print(mytupple)

#create list
mylist = [1, 2, 3, 4, 5]

# modify list to be 10
mylist[0] = 10

# create tuple
list = (1, 2, 3, 4, 5)

# modify value to be 10
list[0] = 10

print(mylist, list)

# Dictionaries
# keys, and values
# Easy to remember
azim_dict = {

    "Name": "Azim",
    "Age": 22,
    "Adult": True,
    "StudentStatus": "PhD"

}

print(azim_dict["Name"])

# sets
# Problem, duplicate values
mylist = [1, 1, 1, 1, 2, 2, 3, 4, 4, 5]

myset = set(mylist) # eliminates duplicates

print(myset)