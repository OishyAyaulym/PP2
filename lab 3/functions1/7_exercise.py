def has_33(n):
    for i in range(len(n)-1):
        if n[i]==3 and n[i+1]==3:
            return True
    return False
a=input("enter numbers:")
b=list(map(int, a.split()))
print(has_33(b))