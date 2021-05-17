# Guess the number game.
# GuessNumber.py

import random

num_guesses = 0
user_name = input("Hi: What is your name? ")
number = random.randint(1,20)
print("Welcome, {}! Guess number between 1 and 20.".format(user_name))

while num_guesses < 6:

    guess = int(input("Take a guess?"))
    num_guesses += 1

    if guess < number:
        print("Number too low")

    if guess > number:
        print("Number too high")

    if guess == number:
        break

if guess == number:
    print("Woopee!")
else:
    print("Loser!!!")
    
