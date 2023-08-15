import random

def random_number(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # It could also be high because low = high

        feedback = input(f"The guess is {guess}, if it is too high then press 'H', if it is too low then press 'L', and if it is correct press 'C': ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The guess {guess} is correct")

random_number(100)
