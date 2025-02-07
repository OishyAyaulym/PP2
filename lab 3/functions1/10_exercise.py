def uniq(n):
    result=[]
    for num in n:
        if num not in result:
            result.append(num)
    return result
a=input("enter numbers:")
b=list(map(int, a.split()))
print(uniq(b))