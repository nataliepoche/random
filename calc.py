import math


def main():
    #We're creating a logarithm calculator
    #Specifically with a custom base and argument
    #let's say we wanted to find log2(8) =
    # The result should be 3 from our progress
    base = int(input("Enter the base for your logarithm: "))
    argument = int(input("Enter the argument for your logarithm"))
    #loga(b) = logm(b)/logm(a)
    # natural log, i.e. ln
    if base <= 0 or argument <= 0:
        print("Cannot calculate goodbye")
    else:
        exponent = math.log(argument) / math.log(base)
        print(f"{exponent: .2f}")


    print("Hello word")

if __name__ == "__main__":
    main()