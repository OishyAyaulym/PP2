import math
class Point:
    def __init__(self):
        self.x = float(input("enter x: "))
        self.y = float(input("Enter y: "))
    def show(self):
        print(f"point coordinates: ({self.x}, {self.y})")
    def move(self):
        self.x = float(input("enter new x: "))
        self.y = float(input("enter new y: "))
        print(f"point moved to: ({self.x}, {self.y})")
    def dist(self, othpoint):
        return math.sqrt((self.x - othpoint.x) ** 2 + (self.y - othpoint.y) ** 2)
print("enter coordinates for the first point:")
p1 = Point()
print("enter coordinates for the second point:")
p2 = Point()
p1.show()
p2.show()
print("distance between points:", p1.dist(p2))
print("move the first point:")
p1.move()
p1.show()