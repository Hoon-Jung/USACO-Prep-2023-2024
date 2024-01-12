#O(n log n) <-- python sorted function

cows = int(input())
pays = input().split()
perp = {}

for i in range(cows):
    try:
        perp[pays[i]] += 1
    except:
        perp[pays[i]] = 1

j = sorted(map(int, perp.keys()))
totalcows = 0
profit = 0
maxprof = 0
maxcost = 0

for i in range(len(j)-1, -1, -1):
    totalcows += perp[str(j[i])]
    profit = totalcows * j[i]
    if profit >= maxprof:
        maxprof = profit
        maxcost = j[i]


print(maxprof, maxcost)