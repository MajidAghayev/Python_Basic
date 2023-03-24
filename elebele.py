import heapq

def main():

    n = int(input("Enter number of elements  : "))


    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    average = sum(a)/len(a)
    print("\nList is - ", a)
    print("average value is : ", average)
    top3 = heapq.nlargest(3, zip(a))
    print(top3)

while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break



