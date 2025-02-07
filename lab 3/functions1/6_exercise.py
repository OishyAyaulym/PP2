"""def rev_str(s):
    a=s.split()
    result=[]
    for i in range(len(a)):
        result.append(a[len(a)-i-1])
    print(" ".join(result))
b=input("enter string: ")
rev_str(b)"""
def rev_str(s):
    print(" ".join(s.split()[::-1]))
a=input("enter string: ")
rev_str(a)