lst=[]
dict={}
lst.append(10.05)
lst.append(0.8)
lst.append(11.2)
lst.append("Python")
lst.append(777)
lst.append("txt")
lst.append("Riga")
a = lst
b = [x for x in a if type(x)==float] #list with only decimal numbers
print("decimal numbers are: ",b)
average = sum(b)/len(b)
print("average for decimal is : ",average)

def diction():
    d = [x for x in a if type(x) == str]  #list with only str in it
    print("strings are : ",d)
    second=d[1] # second element of strings
    print("second string is: ",second)
    for i in second:
        if dict.get(i) == None:
            dict[i] = 1
        else:
            dict[i] += 1

    print("number of characters in",second,"are: ",dict) #number of characters
diction()




