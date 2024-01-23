#1 hour 19 min (only because I had to solve it twice)

fil = open("balancing.in")
ncows, highestx = fil.readline().split()


def checklines(vals, a, b):
    cowsperquad = [0, 0, 0, 0]
    for j in range(len(vals)):
        if cowslist[j][0] < a and cowslist[j][1] < b:
            cowsperquad[2] += 1
        elif cowslist[j][0] < a and cowslist[j][1] > b:
            cowsperquad[1] += 1
        elif cowslist[j][0] > a and cowslist[j][1] < b:
            cowsperquad[3] += 1
        else:
            cowsperquad[0] += 1
    return max(cowsperquad)


setxs = set()
setys = set()
cowslist = []
for i in range(int(ncows)):
    x, y = fil.readline().split()
    cowslist.append([int(x), int(y)])
    setxs.add(int(x))
    setys.add(int(y))

ans = 101
for j in setxs:
    for n in setys:
        abc = checklines(cowslist, j+1, n+1)
        if ans > abc:
            ans = abc

print(ans, file=open("balancing.out", "w"))