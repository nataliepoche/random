def main():
    # time complexity
    n = [2, 4, 5, 7, 8, 9, 10] # took this from input, i.e length may not be the same
    m = [1, 2, 4, 0, 1, 5] # assume this input is unrelated to, length may vary

    # what is the worst case time complexity for this algorithm?
    # O(n^2), O(100n) = O(n)
    for i in range(100): # running 100 times, adds the 100 to O(n) = O(100n)
        for j in range(len(n)): # This is O(n)
            print("Hi")

    # what is the worst case time complexity for this algorithm?
    # O(10000 * 100)
    for i in range(10000):
        for j in range(100):
            print("Hi")

    # what is the worst case time complexity for this algorithm?
    # O(n*m) = O(nm)
    for i in range(len(n)):
        for j in range(len(m)):
            print("Hi")

    # what is the worst case time complexity for this algorithm?
    # O(n + m)
    for i in range(len(n)):
        print("Hi")
    for j in range(len(m)):
            print("Hi")

    # what is the worst case time complexity for this algorithm?
    # O(leg2n) = O(logn)
    # len(n) = 8
    # i = 8, 4, 3, 1, 0
    i = len(n)
    while i > 0:
        print("Hi")
        i //= 2

if __name__ == "__main__":
    main()