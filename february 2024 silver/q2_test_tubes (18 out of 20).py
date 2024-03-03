def simplify(tube1, tube2):
    prev1 = tube1[0]
    prev2 = tube2[0]
    newtube1 = []
    newtube2 = []
    for i in range(len(tube1)-1):
        if tube1[i+1] != prev1:
            newtube1.append(prev1)
            prev1 = tube1[i+1]
        if tube2[i+1] != prev2:
            newtube2.append(prev2)
            prev2 = tube2[i+1]
    newtube1.append(prev1)
    newtube2.append(prev2)
    return newtube1, newtube2


def solve1(t1, t2):
    ans = 0
    t1, t2 = simplify(t1, t2)
    ans += len(t1) + len(t2) - 2
    if t1[0] == t2[0]:
        ans += 1
    if ans > 1:
        ans += 1
    return ans


def solve2and3(t1, t2):
    b = []
    moves = []
    t1, t2 = simplify(t1, t2)

    if t1[0] == t2[0]:
        if t1[0] == "1":
            t2.insert(0, "2")
        else:
            t2.insert(0, "1")

    if t1[-1] == t2[-1]:
        if len(t1) > 1:
            t1.pop()
            moves.append([1, 2])
        else:
            t2.pop()
            moves.append([2, 1])

    if len(t1) + len(t2) == 2:
        return moves
    if len(t1) > 1:
        b.append(t1.pop())
        moves.append([1, 3])
    else:
        b.append(t2.pop())
        moves.append([2, 3])


    if t2[0] != b[0]:
        for _ in range(len(t2)-1):
            if t1[-1] == t2[-1]:
                t2.pop()
                moves.append([2, 1])
            else:
                t2.pop()
                moves.append([2, 3])
        for _ in range(len(t1)-1):
            if t2[-1] == t1[-1]:
                t1.pop()
                moves.append([1, 2])
            else:
                t1.pop()
                moves.append([1, 3])
    else:
        for _ in range(len(t1)-1):
            if t2[-1] == t1[-1]:
                t1.pop()
                moves.append([1, 2])
            else:
                t1.pop()
                moves.append([1, 3])
        for _ in range(len(t2)-1):
            if t1[-1] == t2[-1]:
                t2.pop()
                moves.append([2, 1])
            else:
                t2.pop()
                moves.append([2, 3])
    if b[0] == t1[0]:
        moves.append([3, 1])
    else:
        moves.append([3, 2])
    return moves
    



for _ in range(int(input())):
    N, solvecase = map(int, input().split())
    tube1 = input()
    tube2 = input()
    print(solve1(tube1, tube2))
    if solvecase != 1:
        for x, y in solve2and3(tube1, tube2):
            print(x, y)
