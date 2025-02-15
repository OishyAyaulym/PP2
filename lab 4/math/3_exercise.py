import math
numside=int(input("Input number of sides: "))
lenside=float(input("Input the length of a side: "))
area=(numside*lenside**2)/(4*math.tan(math.pi/numside))
print("The area of the polygon is: ",area)