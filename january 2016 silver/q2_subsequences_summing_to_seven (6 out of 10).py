fil = open("div7.in")
n = int(fil.readline())
prefixsumarr = [0 for j in range(n+1)]
for i in range(1, n+1):
    prefixsumarr[i] += prefixsumarr[i-1] + int(fil.readline())


maxarrlen = 0
arrlen = n+1
while True:
    num = prefixsumarr.pop(0)
    arrlen -= 1
    for m in range(arrlen):
        if (prefixsumarr[-(m+1)] - num) % 7 == 0:
            maxarrlen = max(arrlen - m, maxarrlen)
            break
    if maxarrlen >= arrlen:
        break

print(maxarrlen, file=open("div7.out", "w"))