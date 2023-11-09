def bubble_sort(num_list: list) -> None:
    print(f"The original list is {num_list}")

    # Iterating n-1 number of times
    for i in range(len(num_list) - 1):
        swapped = False
        # Iterating n-1 - i number of times
        for j in range(len(num_list) - i - 1):
            # If the left element is greater than the right element, swap their places
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swapped = True
        print(f"The list is {num_list} after pass number {i + 1}")
        if not swapped:
            return


def insertion_sort(num_list: list) -> None:
    print(f"The original list is {num_list}")

    # Begin iterating at index 1, i.e. i represents the start of the unsorted region
    for i in range(1, len(num_list)):
        first_unsorted = num_list[i]
        # j is the last value of the sorted region
        j = i - 1
        while j >= 0 and first_unsorted < num_list[j]:
            # if first_unsorted is less than num_list[j], move the element at index j to the right one
            num_list[j + 1] = num_list[j]
            j -= 1
        # put the first_unsorted value in the correct spot in the sorted region
        num_list[j + 1] = first_unsorted
        print(f"The list is {num_list} after pass number {i}")
    return


def main():
    bubble_sort([3, 1, 4, 7, 2, 6])
    insertion_sort([3, 1, 4, 7, 2, 6])


if __name__ == "__main__":
    main()