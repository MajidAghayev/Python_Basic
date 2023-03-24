import math
import sys
def main():
    x = int(input("please enter value for x : "))

    a = 3*x**2+4*x

    b = x + x**-1

    print("value for a :",a,"value for b :",b)
    if a < 10 :
        if a + b < 0:
            sys.exit("in frist expression program has negative value for root, please run program again and enter another number")
        else:
         Y1 = math.sqrt(a+b)

        print("value for first expression Y1 is : ",Y1)


    else:

        Y2 = ((1 - a) / 10) + b
        print("value for second expression Y2 is : ",Y2)


while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break

