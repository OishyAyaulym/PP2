import re
a=input("input: ")
camcase=re.sub(r'_([a-z])', lambda x: x.group(1).upper(), a)
print(camcase)