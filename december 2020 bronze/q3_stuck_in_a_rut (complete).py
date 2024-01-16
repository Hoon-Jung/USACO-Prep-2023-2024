#1 hour 30 min

fil = int(input())
east = []
north = []
#[x, y, index, is hit] ^^^
ans = [1000000001 for i in range(fil)]

for i in range(fil):
    j = input().split()
    if j[0] == "E":
        east.append([int(j[1]), int(j[2]), i, False])
    else:
        north.append([int(j[1]), int(j[2]), i, False])


#check amongst easts
for n in range(len(east)):
    for m in range(n+1, len(east)):
        if east[n][1] == east[m][1]:
             if east[n][0] > east[m][0]:
                 ans[east[m][2]] = min(ans[east[m][2]], (east[n][0] - east[m][0]))
             else:
                 ans[east[n][2]] = min(ans[east[m][2]], (east[m][0] - east[n][0]))


#check amongst norths
for n in range(len(north)):
    for m in range(n+1, len(north)):
        if north[n][0] == north[m][0]:
             if north[n][1] > north[m][1]:
                 ans[north[m][2]] = min(ans[north[m][2]], (north[n][1] - north[m][1]))
             else:
                 ans[north[n][2]] = min(ans[north[m][2]], (north[m][1] - north[n][1]))


def flip(a):
    t = a[0]
    a[0] = a[1]
    a[1] = t
    return a


north.sort()
east = list(map(flip, east))
east.sort()
east = list(map(flip, east))


for i in range(len(east)):
    for j in range(len(north)):
        if east[i][0] < north[j][0] and east[i][1] > north[j][1] and not(north[j][3]) and not(east[i][3]):
            if east[i][1] - north[j][1] > north[j][0] - east[i][0]:
                ans[north[j][2]] = min(ans[north[j][2]], (east[i][1] - north[j][1]))
                north[j][3] = True
            elif east[i][1] - north[j][1] < north[j][0] - east[i][0]:
                ans[east[i][2]] = min(ans[north[j][2]], (north[j][0] - east[i][0]))
                east[i][3] = True


for i in range(len(ans)):
    if ans[i] > 1000000000:
        print("Infinity")
    else:
        print(ans[i])