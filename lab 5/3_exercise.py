import re
a=input("input: ")
pattern=r'[a-z]+_[a-z]+'
n=re.findall(pattern, a)
print(n)