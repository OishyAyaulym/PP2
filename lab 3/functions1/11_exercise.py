def palindrome(str):
    s=str[::-1]
    if s==str:
        return True
    return False
a=input("enter: ")
print(palindrome(a))