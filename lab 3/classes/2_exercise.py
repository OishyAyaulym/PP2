class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self):
        self.length=float(input("enter length: "))
    def area(self):
        return (self.length**2)
shape=Shape()
print(shape.area())
square=Square()
print(square.area())