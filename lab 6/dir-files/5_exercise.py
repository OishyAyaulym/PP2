import os
list = list(input().split())
with open('test.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')