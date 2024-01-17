#40 mins (woulda been 20 min if the inputs didn't have spaces at the ends of it)

fil = open("censor.in")

text = fil.readline()
search = fil.readline()
text = text[0:-1]
search = search[0:-1]
slen = len(search)
newstring = ""

for i in range(len(text)):
    newstring += text[i]
    if (newstring[-slen::] == search) and len(newstring) >= slen:
        newstring = newstring[0:len(newstring)-slen]

print(newstring, file=open("censor.out", "w"))