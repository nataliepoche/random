# collects inputs
num_1 = float(input("Enter first operand: "))
num_2 = float(input("Enter second operand: "))

# prints menu
print("Calculator Menu")
print("-" * 15)
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
action = input("Which operation do you want to perform?")

# does the computations
if action == "1": # addition
    result = num_1 + num_2
    print(f"The result of the operation is {result}. Goodbye!")
elif action == "2": # subtraction
    result = num_1 - num_2
    print(f"The result of the operation is {result}. Goodbye!")
elif action == "3": # multiplication
    result = num_1 * num_2
    print(f"The result of the operation is {result}. Goodbye!")
elif action == "4": # division
    result = num_1 / num_2
    print(f"The result of the operation is {result}. Goodbye!")
else: # if it's any other command
    print("Error: Invalid selection! Terminating program.")