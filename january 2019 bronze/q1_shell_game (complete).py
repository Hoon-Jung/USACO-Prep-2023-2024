# 1 2 3
# after swaps find ball
# for loop for all cases to store = O(n) <-- n <= 100
# one for loop which tracks all three cases at once = O(n) <-- n<= 100
# total big O = O(2n)

# dictionary d = {1: 1, 2: 2, 3: 3}
# if statement

def swap(cup1, cup2, cups):
    temp = cups[cup1]
    temp2 = cups[cup2]
    cups[cup1] = temp2
    cups[cup2] = temp
    return cups


fil = open("shell.in")
hm = int(fil.readline())
cups = {"1": 1, "2": 2, "3": 3}
scores = [0, 0, 0]
for i in range(hm):
    inp = fil.readline().split()
    cups = swap(inp[0], inp[1], cups)
    scores[cups[inp[2]]-1] += 1

print(max(scores), file=open("shell.out", "w"))