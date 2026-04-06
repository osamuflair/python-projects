#A number guessing game
import random

def main():
    print("Welcome to the Game.\nTry to guess a number from 1 to 100, let's see how long it'll take you to guess my number")
    secret = random.randint(1, 100)
    i = 0
    while 1:
        try:
            guess = int(input("guess: "))
        except ValueError:
            print("Please enter a number!")
            continue
        
        if guess>100 or guess<1:
            print("INVALID GUESS")
            continue
        i+=1

        if guess == secret:
            print(f"CONGRATULATIONS!!\nYou got it right after {i} trials")
            break
        elif guess > secret:
            print ("Number is lower")
        else:
            print("Number is higher")
main()