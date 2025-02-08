def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
nums = list(map(int, input("enter numbers: ").split()))
prime_nums = list(filter(lambda x: prime(x), nums))
print("Prime numbers:", prime_nums)