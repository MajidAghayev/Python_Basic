# open file in write mode
file1 = open("file.txt", "w")

# write lines in file
file1.write("Hello there,\nHow are you?\n")
file1.close()

# open the file in read mode
file1 = open("file.txt", "r")

# read text from file
text = file1.read()

# remove "\n" from the text
res = str.replace(text, "\n", "")

# separation of every second line
list1 = res.split("\n")

# replace letters with capital letters in every second line
for i in range(1, len(list1), 2):
    list1[i] = list1[i].upper()

# open file in append mode
file1 = open("file.txt", "a")

# append text to the file
for i in range(len(list1)):
    file1.write(list1[i] + "\n")

# close the file
file1.close()