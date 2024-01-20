fil = open("billboard.in")

#assuming rect 1 is to the left
def overlap(coor1, coor2, len2):
    if coor2 - len2 >= coor1:
        return 0
    if coor2 - coor1 < 0:
        return len2
    else:
        return (len2 - (coor2 - coor1))


rect1 = fil.readline().split()
rect2 = fil.readline().split()
rect3 = fil.readline().split()
rect1 = list(map(int, rect1))
rect2 = list(map(int, rect2))
rect3 = list(map(int, rect3))
total = ((rect1[2] - rect1[0]) * (rect1[3] - rect1[1])) + ((rect2[2] - rect2[0]) * (rect2[3] - rect2[1]))

if rect1[0] <= rect3[0]:
    x = overlap(rect1[2], rect3[2], rect3[2] - rect3[0])
else:
    x = overlap(rect3[2], rect1[2], rect1[2] - rect1[0])

if rect1[1] <= rect3[1]:
    y = overlap(rect1[3], rect3[3], rect3[3] - rect3[1])
else:
    y = overlap(rect3[3], rect1[3], rect1[3] - rect1[1])

total -= x*y

if rect2[0] <= rect3[0]:
    x = overlap(rect2[2], rect3[2], rect3[2] - rect3[0])
else:
    x = overlap(rect3[2], rect2[2], rect2[2] - rect2[0])

if rect2[1] <= rect3[1]:
    y = overlap(rect2[3], rect3[3], rect3[3] - rect3[1])
else:
    y = overlap(rect3[3], rect2[3], rect2[3] - rect2[1])

total -= x*y

print(total, file=open("billboard.out", "w"))