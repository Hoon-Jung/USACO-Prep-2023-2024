fil = open("helpcross.in")
c, n = map(int, fil.readline().split())
chickens = []
cows = []
for i in range(c):
    chickens.append(int(fil.readline()))
for j in range(n):
    cows.append(list(map(int, fil.readline().split())))

cows.sort(key=lambda x: x[1], reverse=True)

ccounter = 0
for l in range(n):
    if chickens[ccounter] > 