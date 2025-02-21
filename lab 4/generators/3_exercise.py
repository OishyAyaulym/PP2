def div3_4(N):
    for num in range(0,N+1):
        if num%12==0:
            yield num
a=int(input("enter a: "))
for num in div3_4(a):
    print(num)