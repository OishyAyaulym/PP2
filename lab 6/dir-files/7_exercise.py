with open("test.txt", 'r') as src, open("test1.txt", 'w') as dest:
    dest.write(src.read())