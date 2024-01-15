#32 min

fil = open("cbarn.in")
j = int(fil.readline())
poss = [0 for o in range(j)]

for i in range(j):
    barn = int(fil.readline())
    # print(barn)
    for n in range(j):
        poss[n] += barn*((i+n) % j)

print(min(poss), file=open("cbarn.out", "w"))