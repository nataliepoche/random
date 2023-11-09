def selection_sort(myList): # selection sort
    for i in range(len(myList)):
        min_idx = i
        for j in range(i + 1, len(myList)):
            if myList[min_idx] > myList[j]:
                min_idx = j
        myList[i], myList[min_idx] = myList[min_idx], myList[i]
    print(myList)

def bubble_sort(myList):
    n = len(myList) # 6
    for i in range(n-1): #
        for j in range(0, n-i-1): # n-i-1 means runs algorithm certain number of times
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    print(myList)

def selection_sort(myList):
    for i in range(1, len(myList)):
        key = myList[i]
        j = i-1
        while j>= 0 and key < myList[j]:
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = key
    print(myList)



if __name__ == "__main__":
    # sort() can sort lists, but interviews specifically ask not to use this
    myList = [25, 11, 56, 12, 7, 99]
    print(myList)

    myList.sort()  # sort
    print(myList)

    myList.sort(reverse=True)  # sorts in reverse order
    print(myList)

    selection_sort(myList)
    bubble_sort(myList)
    selection_sort(myList)