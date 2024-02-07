fil = open("angry.in")
n = fil.readline()
bales = []


def blasted(spots, radius):
    blast = []
    for i in spots:
        blast += list(range(i-radius, i+radius+1))
    return set(blast)


for i in range(int(n)):
    bales.append(int(fil.readline()))

maxblast = 0
for j in range(len(bales)):
    keepgoing = True
    exploded = [bales[j]]
    temp = bales.copy()
    r = 1
    excount = 0
    while keepgoing:
        kg = True
        texplode = blasted(exploded, r)
        exploded = []
        counter = 0
        while kg:
            if counter >= len(temp):
                    kg = False
            elif temp[counter] in texplode:
                exploded.append(temp[counter])
                excount += 1
                temp.pop(counter)
            else:
                counter += 1
        if exploded == []:
            break
        r += 1
    maxblast = max(maxblast, excount)


print(maxblast, file=open("angry.out", "w"))
