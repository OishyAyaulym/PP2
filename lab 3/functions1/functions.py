import math
def vol(a):
    return (4/3*(math.pi)*(a**3))

def palindrome(str):
    s=str[::-1]
    if s==str:
        return True
    return False