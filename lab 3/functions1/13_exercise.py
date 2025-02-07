import random
def guessnum():
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num=random.randint(1,20)
    sum=0
    isit=True
    while isit:
        print("Take a guess")
        n=int(input())
        sum+=1
        if n==num:
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            isit=False
            break
        if n>num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
guessnum()