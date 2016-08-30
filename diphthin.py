ospd = open("newDict.txt").read().split("\n")
nospd = []
for word in ospd:
    nospd.append(word.strip())
from itertools import permutations as p
from string import ascii_uppercase as a_u
diphths = ["".join(i) for i in p(list(a_u), 2)]
for i in a_u:
    diphths.append(i*2)
for i in diphths:
    with open(i+".txt", "w"):
        pass
    dfile = open(i+".txt", "w")
    for word in nospd:
        if word[:2] == i:
            pass
            dfile.write(word)
            dfile.write("\n")
    dfile.close()
    




