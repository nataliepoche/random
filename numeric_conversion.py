import math
def menu(): # Prints the menu
    print("Decoding Menu")
    print("-" * 13)
    print("1. Decode hexadecimal \n2. Decode binary \n3. Convert binary to hexadecimal \n4. Quit")

def hex_char_decode(digit): # decodes hexadecimal, sets base to 16
    dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14,
            "f": 15}  # Sets the numeric hexadecimal dictionary
    if digit.isnumeric():  # If the digit is numeric
        digit = int(digit) # Sets the numeric value to an integer
    else:
        digit = int(dict[digit]) # Sets the non-numeric value to it's numeric counter part
    return digit # Returns the value

def hex_string_decode(hex):
    decoded = 0 # starts to keep track of decoded value
    power = 0 # Starts counting the power for the loops
    base = 16 # Keeps the hex base
    if hex.startswith("0x"): # If the hexidecimal starts with 0x
        hex = hex.replace("0x", "") # Gets rid of 0x
    else: # If no 0x value, stays the same
        hex = hex
    for digit in hex[::-1]: # Starts a for loop to go number by number in backwards order
        convert = hex_char_decode(digit) * base ** power # Converts the hexidecimal to it's numeric value and multiblies it by powered base
        decoded += convert # Adds results to keep track of final
        power += 1 # Adds powers together
    return decoded # Returns result

def binary_string_decode(binary): # Decode binary string
    total = 0 # Starts to keep track of total
    power = 0 # Starts to keep track of power
    base = 2 # assigns base
    if binary.startswith("0b"): # If the hexidecimal starts with 0b
        binary = binary.replace("0b", "") # Gets rid of 0b
    else: # if there's no 0x
        binary = binary # Binary is binary
    for digit in binary[::-1]: # Allows to go line by line, reversing the order
        total += int(digit) * base ** power # Turns it into a number and multiplies by it's based power while keeping track of the total
        power += 1 # keeps track of the power
    return total # Returns the results

def binary_to_hex(binary): # converts binary to hexidecimal
    remainder_list = [] # creates a remainder list to keep track of values
    hex = [] # Creates a hex list to put together
    quotient = binary_string_decode(binary) # decodes binary value
    while quotient > 0: # Creates a loop to pick apart numeric pieces to convert
        remainder = quotient % 16 # Returns the remainder amount
        remainder_list.append(remainder) # Adds the remainder to the remainder list
        quotient = quotient // 16 # Gives the number dividble by 16
    for character in remainder_list[::-1]: # Creates a loop to go number by number in list backwards
        if 0 <= character <=9: # sets numeric value of list
            character = str(character)
        # sets hex character for list
        elif character == 10:
            character = "A"
        elif character == 11:
            character = "B"
        elif character == 12:
            character = "C"
        elif character == 13:
            character = "D"
        elif character == 14:
            character = "E"
        elif character == 15:
            character = "F"
        hex.append(character) # Adds characters and numbers to the hex list
    convert = "".join(hex) # joins the items in hex list into one string
    return convert # returns result

condition = True

if __name__ == "__main__":
    while condition == True: # Creates the loop
        menu() # prints the menu
        choice = input("Please enter an option: ") # Inputs option
        if choice == "1": # Decodes a hexadecimal
            hex = input("Please enter the numeric string to convert: ")
            total = hex_string_decode(hex) # gets the value from decoding
            print(f"Result: {total}") # prints decoded value
        elif choice == "2": # Decodes binary
            binary = input("Please enter the numeric string to convert: ")
            total = binary_string_decode(binary) # gets binary decoded value
            print(f"Result: {total}") # prints decoded value
        elif choice == "3": # Converts binary to hex
            binary = input("Please enter the numeric string to convert: ")
            total = binary_to_hex(binary) # gets hex string
            print(f"Return: {total}") # prints hex string
        elif choice == "4": # exits
            print("Goodbye!")
            condition = False