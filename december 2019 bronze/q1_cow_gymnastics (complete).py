fil = open("gymnastics.in")

k, n = fil.readline().split()
cows = [[0 for j in range(int(n))] for b in range(int(n))]

for i in range(int(k)):
    temp = fil.readline().split()
    temp = list(map(int, temp))[::-1]
    da = []
    for j in range(int(n)):
        da.append(temp[j])
        for m in range(int(n)):
            if m+1 not in da:
                cows[m][temp[j]-1] += 1

ans = 0
for l in range(int(n)):
    for s in range(int(n)):
        if int(k) == cows[l][s]:
            ans += 1

print(ans, file=open("gymnastics.out", "w"))