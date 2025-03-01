import re
a=input("input: ")
n=re.sub(r'([a-z])([A-Z])', r'\1_\2', a).lower()
print(n)