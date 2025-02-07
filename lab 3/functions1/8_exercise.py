def spy_game(s):
    seq=[0,0,7]
    for i in range(len(a)-2):
        if s[i:i+3]==seq:
            return True
    return False
a=input("enter numbers:")
b=list(map(int, a.split()))
print(spy_game(b))