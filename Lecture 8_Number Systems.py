# Number systems are to describe numbers
# Binary System - Can only have 1's amd 0's, uses powers of 2
# Ex 00110110 = Start right to left, 0*2^0 + 1*2^1 + 1*2^2 + 0*2^3 + 1*2^4 + 1*2^5 + 0*2^6 + 0*2^7
# = 54

# Hexadecimal System - Base 16, 0 - 15, from 0-9 it's same as decimal system, but after is A, B, C, D, E, F
# Ex 000002A5 = 5*16^0 + 10*16^1 + 2*16^2 + 0*16^3 + 0*16^4 + 0*16^5 + 0*16^6 + 0*16^7

# Lists, want to store multiple variables into one string

friends = ["Joseph", "Glenn", "Sally"] # Creates a collection, a List

print("List Example")
numbers = [5, 10, 15, "Hello", "World", 9.00]
print(numbers)
print(numbers[0]) # Specifies who you want to reference in a list, starts from 0
print(numbers[1])

print("For loop list example")
for number in numbers:
    print(number)

print(len(numbers)) # prints out the number of strings in a list

print("Concatenating lists") # Combining them together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # adds the list into one, but adds variables together

numbers = []
numbers.append("book") # Append adds elements to the lists
numbers.append("cookie")
print(numbers)

# Create a list that contains 1-10, use a for loop
numbers1 = []
for i in range(1, 11):
    numbers1.append(i)

# Create a list that contains 1- 100, use a for loop
numbers2 = []
for i in range(1, 101):
    numbers2.append(i)

print("Create a list that contains 1-10")
print(numbers1)
print("Create a list that contains 1-100")
print(numbers2)

numbers2 = []
for i in range(1, 101):
    if i%2 == 0:  # Creates even intergers
        numbers2.append(i)
print(numbers2)

numbers2 = []
for i in range(1, 101):
    if i%2 == 1:  # Creates odd integers
        numbers2.append(i)
print(numbers2)

# List comprehension
number2 = [i for i in range(1, 101) if i%2 ==1]
print(numbers2)