def exponent(b, e):
    if e == 0:
        return 1
    else:
        return b * exponent(b, e - 1)

def sumation(n): # (n+1)/2
    if n == 1:
        return n
    else:
        return n + sumation(n - 1)

def sum_of_digits(n): # sum of digits
    if n < 10:
        return n
    return sum_of_digits(n // 10) + n % 10 # magic(n//10) extracts last digit
def target_in_list(arr, size, target): # add amount of targets in the list
    if size == 0:
        return 0
    if arr[size-1] == target:
        return 1 + target_in_list(arr, size-1, target)
    return target_in_list(arr, size-1, target)


if __name__ == "__main__":
    print(exponent(4,3))
    print(sumation(5))
    print(sum_of_digits(24187))
    arr = [3, 4, 1, 4, 5, 12, 4]
    target = 4
    print(target_in_list(arr, len(arr), target))