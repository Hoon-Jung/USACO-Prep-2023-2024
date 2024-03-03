#2 hours 30 min

def works(yval, pslopes, positiveslopes):
    max_slopes = []
    for x, y in pslopes:
        max_slopes.append((y - yval) // x)
    max_slopes.sort()
    working = True
    for o in range(len(positiveslopes)):
        if max_slopes[o] < positiveslopes[o]:
            working = False
    return working


def positivesolve(positiveslopes, pslopes):
    positiveslopes.sort()
    lowestyval = min([y for x, y in pslopes])
    # print(positiveslopes)
    lo = lowestyval - positiveslopes[-1] * max([x for x, y in pslopes])
    hi = lowestyval
    while lo < hi:
        mid = (lo + hi + 1) // 2
        # print(lo, mid, hi)
        if works(mid, pslopes, positiveslopes):
            lo = mid
        else:
            hi = mid - 1
    return lo


def posneg(lis, length):
    pos = []
    neg = []
    for j in range(length):
        if lis[j] < 0:
            neg.append(lis[j])
        else:
            pos.append(lis[j])
    return pos, neg


def solve(inp):
    targets = int(inp[0])
    leftx = int(inp[1])
    lefty = []
    pslopes = [] #bottomright
    nslopes = [] #topright
    for _ in range(targets):
        y1, y2, x2 = map(int, input().split())
        lefty.append(y1)
        lefty.append(y2)
        pslopes.append([x2, y1])
        nslopes.append([x2, y2])
    slopes = list(map(int, input().split()))
    positive, negative = posneg(slopes, targets*4)
    lefty.sort()
    if len(positive) < targets or len(negative) < targets:
        return -1
    for n in range(len(lefty)):
        if len(negative) > len(nslopes):
            nslopes.append([leftx, lefty[n]])
        else:
            pslopes.append([leftx, lefty[n]])

    return -(positivesolve([-s for s in negative], [[x, -y] for x, y in nslopes])) - positivesolve(positive, pslopes)


for i in range(int(input())):
    print(solve(input().split()))
