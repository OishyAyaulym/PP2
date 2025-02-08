class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length=float(input("enter the length: "))
        self.width=float(input("enter the width: "))
    def area(self):
        return (self.length*self.width)
rectangle=Rectangle()
print(rectangle.area())