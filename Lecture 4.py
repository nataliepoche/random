# name binding and split
# input.split method, is when variables are seperated by spaces instead of new lines

# transforms the input into a list of strings
first_name, last_name = input().split()
print("First name is", first_name)
print("Last name is", last_name)
# split method uses space as the limitor
# if you add more than the needed values, then it becomes an error

# f-string
print(f"First name is {first_name} \nLast name is {last_name}") #Anything added to {} is treated like code

# comments
# Comments are used for other people to understand your code
"""This is 
multiline comments""" # not a comment, still a string, but the interpreter ignores the string

# Blackjack:

# if statement - cards
