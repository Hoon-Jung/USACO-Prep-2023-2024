alpha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

fil = open("blocks.in")


def removedupes(word1, word2, alp):
    lets = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for i in range(len(word1)):
        if word1.count(word1[i]) > lets[word1[i]]:
            lets[word1[i]] = word1.count(word1[i])
    for j in range(len(word2)):
        if word2.count(word2[j]) > lets[word2[j]]:
            lets[word2[j]] = word2.count(word2[j])
    for n in alp.keys():
        alp[n] += lets[n]
    return alp



for i in range(int(fil.readline())):
    words = fil.readline().split()
    alpha = removedupes(words[0], words[1], alpha)

ans = ""
for i in alpha.keys():
    if i == "z":
        ans += str(alpha[i])
    else:
        ans += str(alpha[i]) + "\n"
print(ans, file=open("blocks.out", "w"))