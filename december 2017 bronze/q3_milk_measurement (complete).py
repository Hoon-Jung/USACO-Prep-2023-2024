#35 mins

days = ["" for i in range(101)]
cows = {"M": 7, "B": 7, "E": 7}
fil = open("measurement.in")
highest = ["M", "B", "E"]
updates = 0

for i in range(int(fil.readline())):
    r = fil.readline().split()
    days[int(r[0])] = r[1][0] + r[2]

for j in range(len(days)):
    if days[j] != "":
        cows[days[j][0]] += int(days[j][1:])
        highestcount = max([cows["M"], cows["B"], cows["E"]])
        newhighest = [j for j in cows.keys() if cows[j] == highestcount]
        if highest != newhighest:
            highest = newhighest
            updates += 1

print(updates, file=open("measurement.out", "w"))