import re
a=input("input: ")
pattern=r'a.*b'
n=re.findall(pattern, a)
print(n)