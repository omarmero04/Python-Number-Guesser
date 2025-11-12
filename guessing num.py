import random
print("________________Welcome to our demo guessing game________________")
num = random.randint(1,10)
tries = int(input("enter the number of tries you want "))
i = 0
while tries > i :
    guess=int(input("enter the guessing number "))
    if num == guess :
        print("Congratulations you got it")
        print(f"you get it right after {i+1} tries")
        break 
    elif num > guess:
        print("try higer number")
        i=i+1
    elif num < guess:
        print("try smaller number")
        i=i+1

if num != guess and tries == i:
 print(f"sorry amigo the number is {num}")