import re
a=input("input: ")
n=re.sub(r'([a-z])([A-Z])', r'\1 \2', a)
print(n)