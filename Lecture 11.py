def consecutive_fours(arr):

    """consecutive_fours(arr) This method will take in an array of integers and return true if the array contains at least 4 consecutive numbers with the same value. Useful for method 2 (count_runs) and 3 (encode_rle).

    Ex: consecutive_fours([3,2,5,4,4,4,5,5,5]) returns False.
    Ex: consecutive_fours([3,2,5,4,4,4,4,7,12]) returns True."""
    count = 1
    for i in range(1,len(arr)): # starts from 1 and continues to end
        print(arr[i - 1], arr[i])  # prints consecutive numbers
        if arr[i-1] == arr[i]: # Checks if there are consecutive numbers
            count += 1 # Addds the count if they are equal
            if count>= 4: return True
        else:
            count = 1 # reinitializes the count, and resets the count
    return False

def sum_by_parity(arr): # should sum up even numbers and sum up odd numbers
    """sum_by_parity(arr) Parity is the formal name for the property of a number being even or odd. This method will take in an array of integers, store the sum of all the values located at even indices in the first index of a new array, then store the sum of all the values located at odd indices in the second index of this new array. Useful for method 4 (get_decoded_length).
    Ex: sum_by_parity([5,12,8,5,3,11,7,2,3,16,4]) returns [30,46]."""
    for i in range(0, len(arr), 2): # Increment indecies by 2
        print(i)

def expand_by_index(arr):
    result = []
    for index in range(0, len(arr)):
        value = arr[index]
        for times in range(0, value):
            result.append(index)
    return result

def expand_by_index_2(arr):
    result = []
    print(list(enumerate(arr)))
    for index, value in enumerate(arr):
        for times in range(0, value):
            result.append(index)
    return result

def numerical_count(my_string):
    count = 0
    for each_char in my_string: # Separates each character
        print(each_char, " ", ord(each_char))
        if ord(each_char) >= 48 and ord(each_char) <= 57:
            count += 1
    print(count)

if __name__ == "__main__":
    print(consecutive_fours([3, 2, 5, 4, 4, 4, 4, 7, 12]))
    print(sum_by_parity([1, 2, 3, 4]))
    print(expand_by_index([2, 1, 3])) # [0,0 1, 2, 2, 2]
    # assert(expand_by_index([2, 1, 3])) == [0, 0, 1, 2, 2, 2]
    print(expand_by_index_2([2, 1, 3, 5, 0]))  # [0,0 1, 2, 2, 2]
    print(numerical_count("Apple35"))