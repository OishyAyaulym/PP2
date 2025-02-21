def func(N):
    for num in range(N,-1,-1):
        yield num
a=int(input("enter a: "))
for num in func(a):
    print(num)