#1 hour 5 min

fil = open("traffic.in")
before = []
rev = []
addsubr = [0, 0]
addsub = [0, 0]
sections = []

for i in range(int(fil.readline())):
    sections.append(fil.readline().split())

for i in range(len(sections)):
    #forward
    if before != [] and (sections[i][0] == "on" or sections[i][0] == "off"):
        if sections[i][0] == "on":
            addsub[0] += int(sections[i][1])
            addsub[1] += int(sections[i][2])
        else:
            addsub[0] -= int(sections[i][2])
            addsub[1] -= int(sections[i][1])
    elif before == [] and sections[i][0] == "none":
        before = [int(sections[i][1]), int(sections[i][2])]
    elif sections[i][0] == "none":
        before[0] += addsub[0]
        before[1] += addsub[1]
        addsub = [0, 0]
        if before[0] < int(sections[i][1]):
            before[0] = int(sections[i][1])
        if before[1] > int(sections[i][2]):
            before[1] = int(sections[i][2])
    
    ri = -(i+1)
    #reverse
    if rev != [] and (sections[ri][0] == "on" or sections[ri][0] == "off"):
        if sections[ri][0] == "off":
            addsubr[0] += int(sections[ri][1])
            addsubr[1] += int(sections[ri][2])
        else:
            addsubr[0] -= int(sections[ri][2])
            addsubr[1] -= int(sections[ri][1])
    elif rev == [] and sections[ri][0] == "none":
        rev = [int(sections[ri][1]), int(sections[ri][2])]
    elif sections[ri][0] == "none":
        rev[0] += addsubr[0]
        rev[1] += addsubr[1]
        addsubr = [0, 0]
        if rev[0] < int(sections[ri][1]):
            rev[0] = int(sections[ri][1])
        if rev[1] > int(sections[ri][2]):
            rev[1] = int(sections[ri][2])


before[0] += addsub[0]
before[1] += addsub[1]

rev[0] += addsubr[0]
rev[1] += addsubr[1]

for i in range(2):
    if before[i] < 0:
        before[i] = 0
    if rev[i] < 0:
        rev[i] = 0


print(str(rev[0]) + " " + str(rev[1]) + "\n" + str(before[0]) + " " + str(before[1]), file=open("traffic.out", "w"))