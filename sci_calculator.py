condition = True
import math

result = 0.0 # Sets the current result to 0.0
loop = 0 # sets the round number to 0
total = 0 # Starts to add all the results together to get the average for option 7

print(f"Current Result: {result}") # Prints current result as 0 initially
# Intitial options
print("Calculator Menu")
print("-" * 15)
print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")

while condition == True:
    # Creates the message window
    menu = input("Enter Menu Selection: ") # Prints the result

    # Execute the options
    if menu == "0": # Ends the process
        print("Thanks for using this calculator. Goodbye!")
        break # Breaks the entire loop
    elif menu == "1": # Adds the values
        num_1 = float(input("Enter first operand: "))
        num_2 = float(input("Enter second operand:"))
        loop += 1 # Adds games
        result = num_1 + num_2 # Executes the addition
        total += result # Adds the results together
        print(f"Current Result: {result}") # Prints results
        print("Calculator Menu")
        print("-" * 15)
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "2": # Subtracts the values
        num_1 = float(input("Enter first operand: "))
        num_2 = float(input("Enter second operand:"))
        loop += 1 # Adds games
        result = num_1 - num_2 # Executes the subtraction
        total += result # Adds the results
        print(f"Current Result: {result}")
        print("Calculator Menu")
        print("-" * 15)
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "3": # Multiplies Values
        num_1 = float(input("Enter first operand: "))
        num_2 = float(input("Enter second operand:"))
        loop += 1 # Adds the number of rounds
        result = num_1 * num_2 # Performs the multiplucation
        total += result # Adds the results
        print(f"Current Result: {result}")
        print("Calculator Menu")
        print("-" * 15)
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "4": # Divides values
        num_1 = float(input("Enter first operand: "))
        num_2 = float(input("Enter second operand:"))
        loop += 1 # Records rounds
        result = num_1 / num_2 # Performs the division
        total += result # Adds the results
        print(f"Current Result: {result}")
        print("Calculator Menu")
        print("-" * 15)
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "5": # Exponential values
        num_1 = float(input("Enter first operand: ")) # Inputs the number
        num_2 = input("Enter second operand:") # Inputs other than numbers

        if num_2 == "RESULT": # Result input for extra credit
            result = num_1 ** total
            loop += 1
            total += result
            print(f"Current Result: {result}")
            print("Calculator Menu")
            print("-" * 15)
            print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
        else:
            num_2 = float(num_2) # Turns inputs into numbers if the input isn't result
            loop += 1 # Records the rounds
            result = num_1 ** num_2 # Applies the exponent
            total += result # Records the results
            print(f"Current Result: {result}")
            print("Calculator Menu")
            print("-" * 15)
            print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "6": # logarithmic values
        num_1 = float(input("Enter first operand: "))
        num_2 = float(input("Enter second operand:"))
        loop += 1 # Records rounds
        result = math.log(num_2, num_1) # Executes logarithm
        total += result # Adds results
        print(f"Current Result: {result}")
        print("Calculator Menu")
        print("-" * 15)
        print("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n 6. Logarithm \n7. Display Average")
    elif menu == "7": # Averages
        if loop == 0: # If there's nothing to average
            print("Error: No calculations yet to average!")
        else: # Averages
            print(f"Sum of calculations: {total:.2f}")
            print(f"Number of calculations: {loop}")
            print(f"Average of calculations: {total / loop:.2f}")
    else: # If selected not one of the options
        print("Error: Invalid selection!")