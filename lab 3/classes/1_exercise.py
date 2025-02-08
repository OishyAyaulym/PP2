class str:
    def __init__(self):
        self.text=""
    def getString(self):
        self.text=input("enter string: ")
    def printString(self):
        print(self.text.upper())
x=str()
x.getString()
x.printString()