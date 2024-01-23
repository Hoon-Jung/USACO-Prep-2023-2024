#8:15
fil = open("cownomics.in")
ans = 0
n, m = fil.readline().split()

scows = []
pcows = []

for r in range(int(n)*2):
    if r // int(n) > 0:
        pcows.append(list(fil.readline())[:-1])
    else:
        scows.append(list(fil.readline())[:-1])

for i in range(int(m)):
    spotty = set()
    plain = []
    for j in range(int(n)):
        spotty.add(scows[j][i])
        plain.append(pcows[j][i])
    
    add = True
    for lets in spotty:
        if lets in plain:
            add = False
    
    if add:
        print(spotty, plain)
        ans += 1


print(ans, file=open("cownomics.out", "w"))    