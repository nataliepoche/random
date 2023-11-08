# Username, password, and calculator

def add(firstNumber, secondNumber):  # Want the def to be at the top
    answer = firstNumber + secondNumber
    return answer  # Returns the value


def subtraction(firstNumber, secondNumber):  # Want the def to be at the top
    answer = firstNumber - secondNumber
    return answer  # Returns the value


def multiplication(firstNumber, secondNumber):  # Want the def to be at the top
    answer = firstNumber * secondNumber
    return answer  # Returns the value


def division(firstNumber, secondNumber):  # Want the def to be at the top
    answer = firstNumber / secondNumber
    return answer  # Returns the value

condition = True
while condition == True: # Starts so the code asks again and again
    name = input("What is your username?")
    password = input("What is your password?")

    if name == "azim" and password == "gators123": # Checks for username and password
        print("Success! You have logged in!")
        break # Exits the while loop

while condition == True:
    "5 + 10"
    # 1. First number
    # 2. Second number
    # 3. Operation

    operation = input("What operation do you want to perform?") # cannot be converted to an integer because input isn't a number
    firstNumber = int(input("What is the first number?")) # converts the string numbers into integers
    secondNumber = int(input("What is the second number?"))

    if operation == "+":
        answer = add(firstNumber, secondNumber)
    elif operation == "-":
        answer = subtraction(firstNumber, secondNumber)
    elif operation == "*":
        answer = multiplication(firstNumber, secondNumber)
    elif operation == "/":
        answer = division(firstNumber, secondNumber)

    print(f"The answer is: {answer}")
    break


# Guess the number
import random # Pycharm add on that generates random numbers

condition = True # Makes the loop able to continue
while condition == True:
    random_number = random.randint(1, 10) # Gives a range
    guess_number = int(input("Guess the number?")) # Convert to integer so it can be checked

    if random_number == guess_number:
        print("Congratulations! You won!")
    else:
        print("Try again!")

# Profile
# Functions are used when there's the same lines with minor changes

condition = True

while condition == True: # Starts the infinite loop
    first_name = input("First Name: ")
    if first_name == "": # if there's no response
        print("Hey! Enter your name again!")
    else:
        break

while condition == True: # Starts the infinite loop
    last_name = input("Last Name: ")
    if last_name == "": # if there's no response
        print("Hey! Enter your name again!")
    else:
        break

while condition == True: # Starts the infinite loop
    email = input("Email: ")
    if email == "": # if there's no response
        print("Hey! Enter your name again!")
    else:
        break

while condition == True: # Starts the infinite loop
    phone = input("Phone: ")
    if phone == "": # if there's no response
        print("Hey! Enter your name again!")
    else:
        break


# Introduction to Functions
# Can be reused and better documented
# Shortens the lines of code

# Example
def provide_options(name):
    print(f"Hello, {name}")
    print("Choose one of the following options:")
    print("1. Register")
    print("2. Quit")

provide_options("Azim")
provide_options("Jack")
provide_options("Victor")