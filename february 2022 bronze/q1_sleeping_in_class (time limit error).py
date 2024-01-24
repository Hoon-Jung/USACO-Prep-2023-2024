#2 hours 15 mins
fil = int(input())


def makegroups(values, group):#return new list and added amount
    te = []
    fin = []
    add = 0
    for i in range(len(values)):
        te.append(values[i])
        su = sum(te)
        if su == group:
            fin.append(group)
            add += len(te) - 1
            te = []
    fin += te
    return fin, add


def minmodsmults(vs, adds):
    total = sum(vs)
    ma = max(vs)
    tem = []
    possibles = []
    for i in range(len(vs)):
        tem.append(vs[i])
        if (total % sum(tem) == 0) and sum(tem) > ma:
            possibles.append(sum(tem))

    if len(possibles) == 1:
        return adds + len(vs) - 1
    else:
        for j in range(len(possibles)):
            made, addedamt = makegroups(vs, possibles[i])
            if len(set(made)) == 1:
                return adds + addedamt
        return adds + len(vs) - 1


def minmods(num, vals):
    vals = list(map(int, vals))
    group = max(vals)
    temp = []
    flist = []
    mods = 0
    for i in range(num):
        temp.append(vals[i])
        if sum(temp) == group:
            flist += [group]
            mods += len(temp) - 1
            temp = []
        elif vals[i] == group:
            flist += temp
            temp = []
    flist += temp
    if len(set(flist)) == 1:
        return mods
    else:
        return minmodsmults(flist, mods)


for i in range(fil):
    a = int(input())
    b = input().split()
    print(minmods(a, b))