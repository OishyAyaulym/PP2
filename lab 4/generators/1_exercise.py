def squarenum(N):
    for num in range(1,N+1):
        yield num**2
a=int(input("enter a: "))
for square in squarenum(a):
    print(square)