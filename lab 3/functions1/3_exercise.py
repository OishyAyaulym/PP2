def solve(numheads, numlegs):
    for c in range(numheads+1):
        r=numheads-c
        if r*4+c*2==numlegs:
            return f"chicken {c}, rabbits {r}"
print(solve(35,94))