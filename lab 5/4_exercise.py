import re
a=input("input: ")
pattern=r'[A-Z][a-z]+'
n=re.findall(pattern, a)
print(n)