#Solved in 30 min (used for USACO Club demonstration so I had to change up my style to get people to understand)
fil = open("speeding.in")

n, m = fil.readline().split()
roadandlimits = []
bessiespeeds = []

for i in range(int(n)):
    line = fil.readline().split() #[road length, speed limit]
    roadlen = int(line[0])
    speedlim = int(line[1])
    roadandlimits.append([roadlen, speedlim])

for j in range(int(m)):
    line = fil.readline().split() #[drive length, speed]
    drivelen = int(line[0])
    speed = int(line[1])
    bessiespeeds.append([drivelen, speed])


roadindex = 0
bessieindex = 0
currentspeedlim = roadandlimits[roadindex][1] #gets initial speed limit
currentbessiespeed = bessiespeeds[bessieindex][1] #gets bessie's initial speed
maxgap = 0 #max amount bessie went over the speed limit
totalroadlen = 0 #Total length of the road traveled so far (combines all previous segments we have traversed through)
totalbessielen = 0 #Total length of the road traveled by Bessie so far (combines all previous segments she has traversed through)

for miles in range(100): #goes from 0-99 so if I add 1 to every mile iteration (miles+1) it becomes 1-100

    if miles+1 > roadandlimits[roadindex][0] + totalroadlen: #If the mile we are on is further than the current stretch we are on
        totalroadlen += roadandlimits[roadindex][0]
        roadindex += 1 #moves to the next segment of the road
        currentspeedlim = roadandlimits[roadindex][1] #changes the speed limit to the limit at the next segment

    if miles+1 > bessiespeeds[bessieindex][0] + totalbessielen: #Same thing as above but for bessie (changes her speed based on where we are)
        totalbessielen += bessiespeeds[bessieindex][0]
        bessieindex += 1
        currentbessiespeed = bessiespeeds[bessieindex][1]

    speeddiff = currentbessiespeed - currentspeedlim #how much bessie is over the speed limit (negative means shes under)
    if speeddiff > 0: #if bessie is actually over the speed limit
        maxgap = max(speeddiff, maxgap) #sets maxgap to whatever is higher: the previous maxgap or the new speeddiff

print(maxgap, file=open("speeding.out", "w"))