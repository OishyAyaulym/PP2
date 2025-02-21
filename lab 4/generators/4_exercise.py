def sqr(a, b):
    for num in range(a,b+1):
        yield num**2
c=int(input("enter c: "))
d=int(input("enter d: "))
for square in sqr(c,d):
    print(square)