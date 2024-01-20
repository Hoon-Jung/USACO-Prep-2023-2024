#10 mins
fil = open("paint.in")
j = fil.readline().split()
b = fil.readline().split()
fence = set()

for i in range(int(j[0]), int(j[1])):
    fence.add(i)
for j in range(int(b[0]), int(b[1])):
    fence.add(j)

print(len(fence), file=open("paint.out", "w"))