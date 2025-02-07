def hist(n):
    for num in n:
        print("*"*num)
a=input("enter numbers:")
b=list(map(int, a.split()))
hist(b)