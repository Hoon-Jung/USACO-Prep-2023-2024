fil = open("mixmilk.in")

lims = ["", "", ""]
cows = ["", "", ""]
lims[0], cows[0] = fil.readline().split()
lims[1], cows[1] = fil.readline().split()
lims[2], cows[2] = fil.readline().split()



def swap(lims, b1, b2, b1ind):
    if b1ind == 2:
        b1ind = -1
    if b1 + b2 <= int(lims[b1ind+1]):
        b2 += b1
        b1 = 0
    else:
        temp = int(lims[b1ind+1]) - b2
        b1 -= temp
        b2 += temp

    return b1, b2


for i in range(100):
    if i%3 == 2:
        cows[i%3], cows[0] = swap(lims, int(cows[i%3]), int(cows[0]), i%3)
    else:
        cows[i%3], cows[i%3 + 1] = swap(lims, int(cows[i%3]), int(cows[i%3 + 1]), i%3)


print(str(cows[0]) + "\n" + str(cows[1]) + "\n" + str(cows[2]), file=open("mixmilk.out", "w"))
