dict = {}
a = input("write here : ")

for i in a:
    if dict.get(i) == None:
        dict[i]=1
    else:
        dict[i]+=1

print(dict)