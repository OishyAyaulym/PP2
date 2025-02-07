from itertools import permutations
def perm(s):
    permlist=["".join(p) for p in permutations(s)]
    for x in permlist:
        print(x)
a=input("enter string: ")
perm(a)