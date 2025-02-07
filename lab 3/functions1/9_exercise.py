import math
def vol(a):
    return (4/3*(math.pi)*(a**3))
rad=float(input("enter radius: "))
print(vol(rad))