import nltk.data
from nltk.tokenize import sent_tokenize

sentences =[]
x = open("pythone.txt", "r+")
for i in x:
    sentences.append(sent_tokenize(i))

x.write(str('\n'.join(sentences[0]))+"\n")
x.write(str('\n'.join(sentences[1]).upper()+ "\n"))
x.write(str('\n'.join(sentences[2]))+"\n")
x.write(str('\n'.join(sentences[3]).upper()+ "\n"))
x.write(str('\n'.join(sentences[4])+"\n"))
x.write(str('\n'.join(sentences[5]).upper()+ "\n"))
x.write(str('\n'.join(sentences[6])+"\n"))

x.close()
x = open("pythone.txt", "r")
print(x.read())






