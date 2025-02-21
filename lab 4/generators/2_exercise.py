def even_nums(N):
    for num in range(0,N+1,2):
        yield num
a=int(input("enter a: "))
print(",".join(str(num) for num in even_nums(a)))