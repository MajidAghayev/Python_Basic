decision = input("If you wanna converto to C print C , for converting to F print F : ")

if decision == "C":
    tempC = float(input("what is the temperature in the room ? "))
    fahrenheit = 32 + tempC * (9 / 5)
    print("the temperature in the room is : ", fahrenheit, "fahrenheit")
elif decision == "F":
    tempF = float(input("temp in room in : "))
    celsius = (tempF - 32) * (5 / 9)
    print("the temperature in the room is : ", celsius, "celsius")
else:
    print("please input either 'C' or 'F'")



