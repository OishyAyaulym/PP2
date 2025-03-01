import re
a=input("input: ")
pattern=r'[ ,.]+'
n=re.sub(pattern, ":",a)
print(n)