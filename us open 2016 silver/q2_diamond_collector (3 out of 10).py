fil = open("diamond.in")
n, k = map(int, fil.readline().split())
# n, k = map(int, input().split())
i = 0
j = n-1
diamonds = []
for m in range(n):
    diamonds.append(int(fil.readline()))
# for m in range(n):
#     diamonds.append(int(input()))


diamonds.sort()
# prev = -1
# maxdia = 0
# secondmaxdia = 0
# for i in range(n):
#     if prev == diamonds[i]:
#         continue
#     ind = i
#     while diamonds[ind] <= k + diamonds[i]:
#         ind += 1
#         if ind >= n-1:
#             break
#     if ind-i >= maxdia:
#         secondmaxdia = maxdia
#         maxdia = ind-i
#     prev = diamonds[i]

# # print(maxdia, secondmaxdia)
# print(maxdia + secondmaxdia, file=open("diamond.out", "w"))


leftmaxes = [0]
rightmaxes = [0]
lenleft = 0
lenright = 0
leftlist = []
rightlist = []
while i <= j:
    leftlist.append(diamonds[i])
    rightlist.append(diamonds[j])
    lenleft += 1
    lenright += 1
    while leftlist[-1] - leftlist[0] > k:
        leftlist.pop(0)
        lenleft -= 1
    while rightlist[0] - rightlist[-1] > k:
        rightlist.pop(0)
        lenright -= 1
    if lenleft > leftmaxes[-1]:
        leftmaxes.append(lenleft)
    if lenright > rightmaxes[-1]:
        rightmaxes.append(lenright)
    i += 1
    j -= 1
    print(leftlist, rightlist)

if rightmaxes[-2] > leftmaxes[-1]:
    print(rightmaxes[-2] + rightmaxes[-1], file=open("diamond.out", "w"))
elif leftmaxes[-2] > rightmaxes[-1]:
    print(leftmaxes[-2] + leftmaxes[-1], file=open("diamond.out", "w"))
else:
    print(leftmaxes[-1] + rightmaxes[-1], file=open("diamond.out", "w"))

# if rightmaxes[-2] > leftmaxes[-1]:
#     print(rightmaxes[-2] + rightmaxes[-1])
# elif leftmaxes[-2] > rightmaxes[-1]:
#     print(leftmaxes[-2] + leftmaxes[-1])
# else:
#     print(leftmaxes[-1] + rightmaxes[-1])