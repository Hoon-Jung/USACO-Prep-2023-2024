fil = open("div7.in")
n = int(fil.readline())
prefixsumarr = [0 for j in range(n+1)]
for i in range(1, n+1):
    prefixsumarr[i] += prefixsumarr[i-1] + int(fil.readline())

for j in range(1, n+1):
    prefixsumarr[j] = prefixsumarr[j] % 7


first_occ = [-1, -1, -1, -1, -1, -1, -1]
last_occ = [-1, -1, -1, -1, -1, -1, -1]
for m in range(1, n+1):
    if first_occ[prefixsumarr[m]] == -1:
        first_occ[prefixsumarr[m]] = m
    else:
        last_occ[prefixsumarr[m]] = m


maxlen = 0
for l in range(7):
    maxlen = max(maxlen, last_occ[l] - first_occ[l])
    

print(maxlen, file=open("div7.out", "w"))