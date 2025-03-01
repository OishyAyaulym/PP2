import re
a=input("input: ")
pattern=r'ab{2,3}'
n=re.findall(pattern, a)
print(n)