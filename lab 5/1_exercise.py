import re
a=input("input: ")
pattern=r'ab*'
n=re.findall(pattern, a)
print(n)