# Ternary Operator
# if/else statements are very long
cats = 5
print("Termnary Operator")
if cats == 5:
    print(f"You have {cats} cats")
else:
    print(f"You don't have {cats} cats")

#if statement using one line og code
print(f"You have {cats} cats") if cats == 5 else print(f"You don't have {cats} cats")
print(f"You have {cats} cats") if cats == 5 else print(f"You don't have {cats} cats")

#Task 1 create a program
# 1. Ask the user if they would like a cake
# 2. If they want a cake, give them a cake
# 3. Otherwise, give them a cookie

print("Task 1")
answer = input("Would you like a cake?")
print(f"Give them a cake") if answer == "yes" else print(f"Give them a cookie")

# for-loops
print("For-loops")
# count to 100
for i in range(1, 100 + 1): # starts from 1 and ends before 100 (aka, 1-99)
    print(i)

# Task 2
# ask for start value
# ask for end value
# use a loop that goes from start to end
print("Taks 2")
start = int(input("What is the start?")) # Need to put int so it can change to a number, or else can't be in the range
end = int(input("What is the end?"))

for i in range(start, end + 1): # the added one is to include the value
    print(i)

# Nested loops
# possible to have loops inside of loops

print("Nested loops")

for i in range(1, 10): # stays the same until the second loop ends
    for j in range(100, 110):
        print(i, j)

# while loops
# like for-loops, can execute print statements a lot of times
# But execute as long as the condition is true

print("While loops")

condition = True

while condition == True:
    print("Hello!")
    break

# Break statement
# asks user if we should stop
# if yes, then "break" the loop

condition = True

while condition:
    answer = input("Would you like to stop?")

    if answer == "yes": # as long as you say no, the program won't stop
        break

# Driver program
# Has: While loops, list of options, users can choose an option

condition = True

while condition == True:
    print("Select one from below:")
    print("1. Say Hello")
    print("2. Watch Lecture")
    print("3. Exit")

    choice = input("Choose")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("I like lectures")
    elif choice == "3":
        break
    else:
        print("Error! Try again")

condition = True

while condition == True:
    print("Choose one of the following")
    print("1. Enter any digit")
    print("2. Enter any character")

    answer = input()

    if answer.isdigit():
        print("This is a digit")
    elif answer == "no":
        break
    else:
        print("This is a character")