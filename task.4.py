import sys
try:
    temp = int(input("what is the temp in room ? :"))

    if 35<=temp<=37 :
        print("everything looks good")
    elif temp<35:
        print("Too cold")
    elif temp>37:
        print("Too hot")

except:
    print("dalbaeb")



