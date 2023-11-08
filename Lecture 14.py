# class example
class Monster:
    def __init__(self):
        self.level = 5
        self.name = "Azim"

    def __str__(self): # prints the output, needs to print out statement to be printed
        return f"My name is {self.name}"

myMonster = Monster()
print(myMonster)

# class overloads
class Monster:
    def __init__(self):
        self.level = 5
        self.name = "Azim"

    def __eq__(self, object): # overloads == to make them equal
        return self.level == object.level # compares level variable of two instances instead of memory addresss
        # return self == object # compares memory addresses

myMonster1= Monster()
myMonster2 = Monster()

print(myMonster1)
print(myMonster2)
print(myMonster1 == myMonster2) # Get a false value

# propert decorator
class Monster:
    def __init__(self):
        self.name = None

    def set_name(self, name): # initialization, sets name/value for variable
        self.name = name

    def get_name(self): # get the value of variable
        return self.name

class Monster:
    def __int__(self):
        self.name = None

    @property # getter
    def name_getter(self):
        return self.name

    @name_getter.setter # setter
    def name_getter(self, name):
        self.name = name

monster1 = Monster()

# monster1.name = "azim", another way to get bane
monster1.name_getter = "azim"

print(monster1.name_getter)

class Human:
    def __init__(self):
        self.name = name

    def say_hi(self):
        print("Hi")

    def say_bye(self):
        print("Bye!")

    def say_name(self):
        print(f"My name is {self.name}")

class Azim(Human):
    def __init__(self):
        self.name = "azim"

a1 = Azim()
a1.say_hi()
a1.say_bye()
a1.say_name()
Azim().say_hi()

class Car():
    def __init__(self):
        self.color = "red"
        self.year = 2019

    def __str__(self):
        return f"this car is from {self.year} and it is {self.color}"

class Motorcycle():
    def __init__(self):
        self.color = "red"
        self.year = 2019

    def __str__(self):
        return f"this Motorcycle is from {self.year} and it is {self.color}"

class Azim:
    def __init__(self):
        self.name = "azim"
        self.car = Car()
        self.motorcycle = Motorcycle()

a1 = Azim()
print(a1.motorcycle)