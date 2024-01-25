#3 hours 15 mins
#does not work O(n^3 i think)
#maybe find prime numbers and eliminate based on that?
fil = int(input())


def makegroups(values, group):#return new list and added amount
    te = []
    fin = []
    add = 0
    su = 0
    for i in range(len(values)):
        te.append(values[i])
        su += values[i]
        if su == group:
            fin.append(group)
            add += len(te) - 1
            te = []
            su = 0
    fin += te
    return fin, add


# def minmodsmults(vs, adds):
#     total = sum(vs)
#     ma = max(vs)
#     tem = []
#     possibles = []
#     for i in range(len(vs)):
#         tem.append(vs[i])
#         if (total % sum(tem) == 0) and sum(tem) > ma:
#             possibles.append(sum(tem))

#     if len(possibles) == 1:
#         return adds + len(vs) - 1
#     else:
#         for j in range(len(possibles)):
#             made, addedamt = makegroups(vs, possibles[i])
#             if len(set(made)) == 1:
#                 return adds + addedamt
#         return adds + len(vs) - 1


# def minmods(num, vals):
#     vals = list(map(int, vals))
#     group = max(vals)
#     temp = []
#     flist = []
#     mods = 0
#     for i in range(num):
#         temp.append(vals[i])
#         if sum(temp) == group:
#             flist += [group]
#             mods += len(temp) - 1
#             temp = []
#         elif vals[i] == group:
#             flist += temp
#             temp = []
#     flist += temp
#     if len(set(flist)) == 1:
#         return mods
#     else:
#         return minmodsmults(flist, mods)


def minmodsmult(length, vs):
    vs = list(map(int, vs))
    total = sum(vs)
    ma = max(vs)
    possibles = []
    su = 0
    if total == 0:
        return 0
    else:
        for i in range(length):
            su += vs[i]
            if (su == 0):
                continue
            elif (total % su == 0) and su >= ma:
                possibles.append(su)
            elif su >= total:
                break

    if len(possibles) == 1:
        return len(vs) - 1
    else:
        for j in range(len(possibles)):
            made, addedamt = makegroups(vs, possibles[j])
            if len(set(made)) == 1:
                return addedamt
        return len(vs) - 1


for i in range(fil):
    a = int(input())
    b = input().split()
    print(minmodsmult(a, b))