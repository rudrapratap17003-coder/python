import random

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

if lower >= upper:
    print("Invalid range!")
    print("Lower limit must be less than upper limit.")

else:
    number = random.randint(lower, upper)

    print("I have selected a number between", lower, "and", upper)
    print("You have 7 chances to guess it.")

    attempts = 0
    guessed = False

    while attempts < 7:
        guess = int(input("Enter your guess: "))

        attempts = attempts + 1

        if guess == number:
            print("Congratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)
            guessed = True
            break

        elif guess < number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

        print("Remaining attempts:", 7 - attempts)

    if guessed == False:
        print("GAME OVER!")
        print("The correct number was:", number)