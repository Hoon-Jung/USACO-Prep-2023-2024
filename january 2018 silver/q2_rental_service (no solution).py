fil = open("rental.in")
n, m, r = map(int, fil.readline().split())
cows = [int(fil.readline()) for i in range(n)]
stores = [list(map(int, fil.readline().split())) for i in range(m)]
rentals = [int(fil.readline()) for i in range(r)]
cows.sort()
stores.sort(key=lambda x: x[1], reverse=True)
rentals.sort(reverse=True)
# for j in range(len(cows)):

print(cows, stores, rentals)