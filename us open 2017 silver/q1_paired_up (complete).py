#1 hour 25 min
fil = open("pairup.in")
ncows = int(fil.readline())
cows = []
cowmax = 0
for oo in range(ncows):
    cows.append(list(map(int, fil.readline().split())))


cows.sort(key=lambda x: x[1])
i = 0
j = ncows-1
while i <= j:
    if cows[i][1] + cows[j][1] > cowmax:
        cowmax = cows[i][1] + cows[j][1]
    if cows[i][0] - cows[j][0] == 0:
        i += 1
        j -= 1
    elif cows[i][0] - cows[j][0] > 0:
        cows[i][0] -= cows[j][0]
        j -= 1
    else:
        cows[j][0] -= cows[i][0]
        i += 1
    if j == i:
        if cows[i][1] + cows[j][1] > cowmax:
            cowmax = cows[i][1] + cows[j][1]
        break

    
    
print(cowmax, file=open("pairup.out", "w"))