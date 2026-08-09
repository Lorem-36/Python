import random

def game():
    guess=random.randint(1,100)
    while True:
        a=input("Guess a number between 1 and 100:")
        if guess==int(a):
            print("You guessed it! game over.")
            break
        elif guess>int(a):
            print("Your guess is low")
        else:
            print("Your guess is high")
game()

