try:
    var = [1, 2, 3]
    var[999]
    var[0]/0
except IndexError as error1:
    print("Index Error")
except ZeroDivisionError as error2:
    print("Dero Division")