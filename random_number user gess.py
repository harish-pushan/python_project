import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess=int(input(f"Enter the guess between 1,{x}: "))
        if guess>random_number:
            print("Sorry the guess is too high try again :")
        elif guess<random_number:
            print("Sorry the guess is too low try again :")
    print("your guess is correct !!")

guess(10)
