import math
import random
import heapq

def main():
    try:
        a = int(input("Enter value for a : "))
        b = int(input("Enter value for b : "))
        a = ((2*a**4)/(6+math.sqrt(a)))*0.5 + 1
        print(a)
    except:
        print("u did something wrong, please enter number")
    lst_a = []
    lst_b = []
    def ameno():

        n = 10
        for x in range(n):
            lst_a.append(random.uniform(a,b))
        print("Randomised list is: ", lst_a)
        print("highest grade is ",max(lst_a))


    ameno()
    lst_b.append(lst_a[::2])
    print("every second number from the first list :", lst_b)
    length = len(lst_a[::2])
    print(length)
    lst_b.sort()
    print("Second Largest element is:", lst_a[::2][length - 2])

    sym_diff = set(lst_a).symmetric_difference(set(lst_a[::2]))
    print("symmetric difference is: ",sym_diff)

    with open("sym_diff=.txt", "w") as h:
        h.write(str(sym_diff))

while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break








